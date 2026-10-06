#!/usr/bin/env python3
"""Session preflight for the handoff layer (specs/08 BP-19).

Parses every record (BP-17), resolves every reference, checks decision and
intake consistency, and reports handoff freshness. Stdlib only.

    python3 scripts/preflight.py            # gates + warnings, exit 1 on gate
    python3 scripts/preflight.py --export   # derived nodes/edges JSON (BP-17)

GATE = the record layer is broken (exit 1). WARN = attention needed (exit 0).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# --- record type registry (BP-17: new types are added HERE, by declaration) --

FIELD_RE = re.compile(r"^([a-z_]+): (.*)$")
REF_FIELDS = ("supersedes", "superseded_by", "affects", "evidence", "builds_on")

RECORD_TYPES = {
    "decision": {
        "file": "progress/decisions.md",
        "heading": re.compile(r"^## (D-\d+) — (.+)$"),
        "id": lambda m: m.group(1),
        "required": ("status", "date", "decided_by", "supersedes",
                     "superseded_by", "affects", "evidence"),
        "status": ("proposed", "accepted", "rejected", "superseded"),
    },
    "intake": {
        "file": "insights_from_other_conversations/INDEX.md",
        "heading": re.compile(r"^## (I-\d+) — (.+)$"),
        "id": lambda m: m.group(1),
        "required": ("status", "date", "received", "source", "file",
                     "affects", "evidence"),
        "status": ("unread", "held", "digested", "applied", "rejected"),
    },
    # Human coherence structure (incubating/human-coherence-intent-anchoring,
    # kit/SPEC.md HC-4, HC-30). Optional: a project without coherence/ passes.
    "intent": {
        "file": "coherence/intent.md",
        "heading": re.compile(r"^## (INT-\d+) — (.+)$"),
        "id": lambda m: m.group(1),
        "required": ("kind", "describes", "status", "confirmed", "evidence",
                     "builds_on", "supersedes", "superseded_by"),
        "status": ("derived", "confirmed", "superseded"),
        "optional": True,
    },
    "sitting": {
        "file": "coherence/owner-log.md",
        "heading": re.compile(r"^## (SIT-\d+) — (.+)$"),
        "id": lambda m: m.group(1),
        "required": ("date", "kind", "confirmed", "decided", "brief"),
        "status": None,
        "optional": True,
    },
    "buildlog": {
        "file": "progress/BUILDLOG.md",
        "heading": re.compile(
            r"^## (\d{4}-\d\d-\d\dT\d\d:\d\d(?::\d\d)?[+-]\d\d:\d\d) · (.+)$"),
        "id": lambda m: "BUILDLOG@" + m.group(1),
        "required": (),
        "status": None,
    },
}

HANDOFF = "progress/HANDOFF.md"
# Files whose prose may cite D-/I-/BUILDLOG@ ids; those citations must resolve.
CITING_FILES = (HANDOFF, "progress/STATUS.md", "DIRECTION.md", "AGENTS.md")
PENDING_FILES = (HANDOFF, "progress/STATUS.md")
HANDOFF_SECTIONS = ("## START HERE", "### FIRST ACT", "### DONE",
                    "### NEXT, IN ORDER", "### FOR THE OWNER",
                    "### EXPECTED OPENING")
INTAKE_DIR = "insights_from_other_conversations"
PROSE_REF_RE = re.compile(
    r"(?<![\w-])((?:D|I|INT|SIT)-\d+|BUILDLOG@\d{4}-\d\d-\d\dT\d\d:\d\d(?::\d\d)?[+-]\d\d:\d\d)")


class Report:
    def __init__(self):
        self.gates: list[tuple[str, str]] = []
        self.warns: list[tuple[str, str]] = []
        self.info: list[str] = []

    def gate(self, msg, remedy):
        self.gates.append((msg, remedy))

    def warn(self, msg, remedy):
        self.warns.append((msg, remedy))


def git(root: Path, *args) -> tuple[int, str]:
    try:
        p = subprocess.run(["git", "-C", str(root), *args],
                           capture_output=True, text=True)
    except FileNotFoundError:
        return 127, ""
    return p.returncode, p.stdout


def parse_ts(s: str) -> datetime | None:
    try:
        dt = datetime.fromisoformat(s.strip())
    except ValueError:
        return None
    return dt if dt.tzinfo else None  # date-only / naive: not comparable


# --- parsing ----------------------------------------------------------------

def parse_records(root: Path, rep: Report) -> dict[str, dict]:
    records: dict[str, dict] = {}
    for rtype, spec in RECORD_TYPES.items():
        path = root / spec["file"]
        if not path.exists() and spec.get("optional"):
            continue
        if not path.exists():
            rep.gate(f"{spec['file']} missing",
                     "restore it from git, or recreate per specs/08 BP-17")
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        current = None
        for n, line in enumerate(lines, 1):
            if line.startswith("## "):
                m = spec["heading"].match(line)
                if not m:
                    rep.gate(f"{spec['file']}:{n} unparseable record heading: {line!r}",
                             f"headings in this file must match {spec['heading'].pattern}")
                    current = None
                    continue
                rid = spec["id"](m)
                if rid in records:
                    rep.gate(f"{spec['file']}:{n} duplicate id {rid}",
                             "ids are never reused (INV-2); give the new record the next id")
                current = {"id": rid, "type": rtype, "title": m.group(2),
                           "file": spec["file"], "line": n, "fields": {},
                           "text": [], "in_fields": True}
                records[rid] = current
                continue
            if current is None:
                continue
            fm = FIELD_RE.match(line) if current["in_fields"] else None
            if fm and rtype != "buildlog":
                current["fields"][fm.group(1)] = fm.group(2).strip()
            else:
                current["in_fields"] = False
                current["text"].append(line)
    for r in records.values():
        r["text"] = "\n".join(r["text"]).strip()
        del r["in_fields"]
    return records


def split_refs(value: str) -> list[str]:
    if value.strip().lower() in ("none", ""):
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


# --- reference resolution (BP-17 grammar) ----------------------------------

class Resolver:
    def __init__(self, root: Path, records: dict[str, dict]):
        self.root = root
        self.records = records
        specs = "\n".join(p.read_text(encoding="utf-8")
                          for p in sorted((root / "specs").glob("*.md")))
        self.req_ids = set(re.findall(r"\*\*([A-Z]+-\d+[a-z]?)\b", specs))
        phases = root / "specs" / "06-phases.md"
        self.passes = set(re.findall(r"^\| (P\d+\.\d+) \|", phases.read_text(
            encoding="utf-8"), re.M)) if phases.exists() else set()
        sharp = root / "spec_sharpening_2026-07-10.md"
        self.findings = set(re.findall(r"^#+ (F-\d+)\b", sharp.read_text(
            encoding="utf-8"), re.M)) if sharp.exists() else set()

    def resolves(self, ref: str) -> bool:
        if re.fullmatch(r"(D|I|INT|SIT)-\d+|BUILDLOG@.+", ref):
            return ref in self.records
        if re.fullmatch(r"F-\d+", ref):
            return ref in self.findings
        if re.fullmatch(r"P\d+\.\d+", ref):
            return ref in self.passes
        if re.fullmatch(r"[A-Z]+-\d+[a-z]?", ref):
            return ref in self.req_ids
        if re.fullmatch(r"[0-9a-f]{7,40}", ref):
            return git(self.root, "cat-file", "-e", ref + "^{commit}")[0] == 0
        return (self.root / ref.rstrip("/")).exists()


# --- checks -----------------------------------------------------------------

def check_records(records, res: Resolver, rep: Report):
    for r in records.values():
        if r["type"] == "buildlog":
            continue
        spec = RECORD_TYPES[r["type"]]
        loc = f"{r['file']}:{r['line']} {r['id']}"
        f = r["fields"]
        for key in spec["required"]:
            if key not in f:
                rep.gate(f"{loc} missing field '{key}'",
                         "add the field line under the heading (BP-17)")
        if f.get("status") and f["status"] not in spec["status"]:
            rep.gate(f"{loc} status '{f['status']}' not in {spec['status']}",
                     "use one of the listed statuses")
        for key in REF_FIELDS:
            for ref in split_refs(f.get(key, "none")):
                if not res.resolves(ref):
                    rep.gate(f"{loc} {key}: '{ref}' does not resolve",
                             "fix the reference (BP-17 grammar) or create its target")


def check_decisions(records, rep: Report):
    decs = {k: r for k, r in records.items() if r["type"] == "decision"}
    for rid, r in decs.items():
        f, loc = r["fields"], f"{r['file']}:{r['line']} {rid}"
        st, by = f.get("status"), f.get("decided_by", "")
        if st == "proposed":
            if by != "pending":
                rep.gate(f"{loc} proposed but decided_by='{by}'",
                         "a proposal is decided_by: pending until the owner answers")
            for marker in ("Options:", "← DEFAULT", "Decision: pending"):
                if marker not in r["text"]:
                    rep.gate(f"{loc} proposal lacks '{marker}'",
                             "proposals need lettered options, a marked default, "
                             "and 'Decision: pending' (BP-15)")
            rep.warn(f"{rid} awaits owner: {r['title']}",
                     f"owner answers in {r['file']}; agents must not act on it")
        elif st in ("accepted", "rejected") and by in ("", "pending"):
            rep.gate(f"{loc} {st} but decided_by='{by}'",
                     "record who decided (owner, or a delegated role)")
        if st == "superseded" and not split_refs(f.get("superseded_by", "none")):
            rep.gate(f"{loc} superseded but superseded_by is none",
                     "name the superseding D- entry")
        for old in split_refs(f.get("supersedes", "none")):
            o = decs.get(old)
            if o and rid not in split_refs(o["fields"].get("superseded_by", "none")):
                rep.gate(f"{loc} supersedes {old}, but {old}.superseded_by lacks {rid}",
                         f"fill superseded_by on {old} (the one allowed edit)")


def check_intake(root: Path, records, rep: Report):
    folder = root / INTAKE_DIR
    registered = {}
    for r in records.values():
        if r["type"] == "intake":
            p = r["fields"].get("file", "")
            registered[p] = r["id"]
            if p and not (root / p).exists():
                rep.gate(f"{r['id']} file '{p}' does not exist",
                         "fix the path, or set status: rejected and note the removal")
    if folder.is_dir():
        for p in sorted(folder.rglob("*")):
            rel = p.relative_to(root).as_posix()
            if p.is_file() and p.name != "INDEX.md" and rel not in registered:
                rep.warn(f"unregistered intake file: {rel}",
                         f"add an I- record to {INTAKE_DIR}/INDEX.md (BP-20)")


def check_citations(root: Path, res: Resolver, rep: Report):
    for name in CITING_FILES:
        p = root / name
        if not p.exists():
            continue
        for ref in sorted(set(PROSE_REF_RE.findall(p.read_text(encoding="utf-8")))):
            if not res.resolves(ref):
                rep.gate(f"{name} cites '{ref}', which does not resolve",
                         "fix the citation or create the record")


def check_pending_claims(root: Path, records, rep: Report):
    """BP-19: each PENDING_FILES `pending_decisions:` line == ledger's proposed set."""
    proposed = {k for k, r in records.items()
                if r["type"] == "decision" and r["fields"].get("status") == "proposed"}
    for name in PENDING_FILES:
        p = root / name
        if not p.exists():
            continue
        lines = [l for l in p.read_text(encoding="utf-8").splitlines()
                 if l.startswith("pending_decisions:")]
        if len(lines) != 1:
            rep.gate(f"{name} has {len(lines)} 'pending_decisions:' lines, needs exactly 1",
                     "add one line: pending_decisions: D-<n>, ... (or none) (BP-19)")
            continue
        claimed = set(split_refs(lines[0].split(":", 1)[1]))
        for d in sorted(claimed - proposed):
            rep.gate(f"{name} lists {d} as pending, but the ledger says it is not",
                     "re-check decisions.md and update the line (BP-18 verify-before-repeat)")
        for d in sorted(proposed - claimed):
            rep.gate(f"{name} omits pending decision {d}",
                     "add it to the pending_decisions line")


REENTRY_GAP_DAYS = 21   # project-set "long gap" (HC-28); change here only


def check_owner(root: Path, records, rep: Report, now: datetime):
    """HC-7, HC-28, BP-22: owner confirmations and the re-entry signal."""
    sits = {k: r for k, r in records.items() if r["type"] == "sitting"}
    for r in records.values():
        if r["type"] == "intent" and r["fields"].get("status") == "confirmed":
            cited = re.findall(r"SIT-\d+", r["fields"].get("confirmed", ""))
            if not cited or any(c not in sits for c in cited):
                rep.gate(f"{r['id']} is confirmed without a matching owner sitting",
                         "only the owner confirms; cite the SIT record of that sitting (HC-7)")
    if not (root / RECORD_TYPES["sitting"]["file"]).exists():
        return
    dated = [(parse_ts(r["fields"].get("date", "")), k) for k, r in sits.items()]
    dated = [(d, k) for d, k in dated if d]
    unread = sorted(k for k, r in records.items()
                    if r["type"] == "intake" and r["fields"].get("status") == "unread")
    if not dated:
        rep.info.append("OWNER no sitting recorded yet; re-entry due: yes")
        rep.warn("RE-ENTRY SIGNAL: no owner sitting recorded",
                 "open with the re-entry frame (BP-22), not with FOR THE OWNER")
        return
    last, sid = max(dated)
    days = max(0, (now - last).days)
    due = days >= REENTRY_GAP_DAYS or bool(unread)
    rep.info.append(f"OWNER last sitting {sid} {last.date().isoformat()} ({days} days ago); "
                    f"unread intake: {', '.join(unread) or 'none'}; "
                    f"re-entry due: {'yes' if due else 'no'}")
    if due:
        why = []
        if days >= REENTRY_GAP_DAYS:
            why.append(f"{days} days since the owner's last sitting")
        if unread:
            why.append(f"unread outside material {', '.join(unread)}")
        rep.warn("RE-ENTRY SIGNAL: " + "; ".join(why),
                 "open with the re-entry frame (BP-22, HC-21), not with FOR THE OWNER")


CLOCK_SLACK_MIN = 2


def record_time(r):
    """The timestamp a record claims: BUILDLOG heading, or a date field."""
    if r["type"] == "buildlog":
        return parse_ts(r["id"].split("@", 1)[1])
    return parse_ts(r["fields"].get("date", ""))


def check_clock(records, rep: Report, now: datetime):
    """Timestamps are evidence only if read from a clock: flag future-dated ones."""
    future = sorted(k for k, r in records.items()
                    if (t := record_time(r)) and (t - now).total_seconds() > CLOCK_SLACK_MIN * 60)
    if future:
        rep.warn(f"{len(future)} record(s) dated in the future: {', '.join(future[:3])}"
                 + (" …" if len(future) > 3 else ""),
                 "read the clock (`date`) when writing timestamps; correct by a new record, not an edit")


def check_handoff(root: Path, records, rep: Report, now: datetime | None = None):
    p = root / HANDOFF
    if not p.exists():
        rep.gate(f"{HANDOFF} missing", "write it per specs/08 BP-14/BP-18")
        return
    head = {}
    for line in p.read_text(encoding="utf-8").splitlines()[:12]:
        m = FIELD_RE.match(line)
        if m:
            head[m.group(1)] = m.group(2).strip()
    lines = p.read_text(encoding="utf-8").splitlines()
    pos = []
    for sec in HANDOFF_SECTIONS:
        hits = [n for n, l in enumerate(lines) if l.startswith(sec)]
        if not hits:
            rep.gate(f"{HANDOFF} lacks section '{sec}'",
                     "rewrite HANDOFF with all BP-14 sections (rules: BP-22)")
        else:
            pos.append(hits[0])
    if len(pos) == len(HANDOFF_SECTIONS) and pos != sorted(pos):
        rep.gate(f"{HANDOFF} sections out of order",
                 "order: " + " → ".join(HANDOFF_SECTIONS) + " (BP-14)")
    as_of = parse_ts(head.get("as_of", ""))
    if as_of is None:
        rep.gate(f"{HANDOFF} lacks a valid 'as_of:' timestamp",
                 "add 'as_of: <ISO ts with offset>' in its first lines (BP-18)")
    else:
        stamps = [parse_ts(r["id"].split("@", 1)[1]) for r in records.values()
                  if r["type"] == "buildlog"]
        limit = now or datetime.now().astimezone()
        newest = max((s for s in stamps
                      if s and (s - limit).total_seconds() <= CLOCK_SLACK_MIN * 60),
                     default=None)
        if newest and newest > as_of:
            rep.warn(f"HANDOFF as_of {as_of.isoformat()} is older than newest "
                     f"BUILDLOG entry {newest.isoformat()}",
                     "re-verify and rewrite HANDOFF at session end (BP-9, BP-18)")
    sha = head.get("verified_at", "")
    if not re.fullmatch(r"[0-9a-f]{7,40}", sha):
        rep.gate(f"{HANDOFF} lacks a valid 'verified_at:' commit",
                 "add 'verified_at: <commit hash>' in its first lines (BP-18)")
        return
    rc, _ = git(root, "cat-file", "-e", sha + "^{commit}")
    if rc != 0:
        rep.gate(f"{HANDOFF} verified_at {sha} is not a commit here",
                 "point verified_at at the commit the claims were checked against")
        return
    _, out = git(root, "diff", "--name-only", sha, "HEAD", "--", "specs", "progress")
    changed = [l for l in out.splitlines() if l and l != HANDOFF]
    if changed:
        rep.warn(f"committed since verified_at {sha}: {', '.join(changed)}",
                 "HANDOFF claims covering these files are void until re-verified (BP-14)")


def check_git(root: Path, rep: Report):
    rc, out = git(root, "status", "--porcelain")
    if rc != 0:
        rep.warn("not a git repository (or git missing)", "run inside the repo clone")
        return
    dirty = [l[3:] for l in out.splitlines() if l]
    if dirty:
        rep.warn(f"dirty tree ({len(dirty)}): {', '.join(dirty)}",
                 "commit, or confirm BUILDLOG journals this dirty state (BP-9)")
    _, hooks = git(root, "config", "--get", "core.hooksPath")
    hook = root / ".githooks" / "commit-msg"
    if hooks.strip() != ".githooks" or not hook.exists():
        rep.warn("commit-msg hook inactive",
                 "owner decision D-10; to activate: git config core.hooksPath .githooks")


# --- export (derived view, BP-17 / INV-1) -----------------------------------

def export(records) -> dict:
    nodes, edges = [], []
    for r in records.values():
        nodes.append({k: r[k] for k in ("id", "type", "title", "file", "fields", "text")})
        for key in REF_FIELDS:
            for ref in split_refs(r["fields"].get(key, "none")):
                edges.append({"src": r["id"], "rel": key, "dst": ref})
        if r["type"] == "buildlog":
            for ref in sorted(set(PROSE_REF_RE.findall(r["text"])) - {r["id"]}):
                edges.append({"src": r["id"], "rel": "mentions", "dst": ref})
    return {"schema_version": 1, "nodes": nodes, "edges": edges}


def run(root: Path, now: datetime | None = None) -> tuple[Report, dict]:
    rep = Report()
    records = parse_records(root, rep)
    res = Resolver(root, records)
    check_records(records, res, rep)
    check_decisions(records, rep)
    check_intake(root, records, rep)
    check_citations(root, res, rep)
    check_pending_claims(root, records, rep)
    now = now or datetime.now().astimezone()
    check_owner(root, records, rep, now)
    check_clock(records, rep, now)
    check_handoff(root, records, rep, now)
    check_git(root, rep)
    return rep, records


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=Path,
                    default=Path(__file__).resolve().parent.parent)
    ap.add_argument("--export", action="store_true",
                    help="print derived nodes/edges JSON instead of the report")
    args = ap.parse_args(argv)
    rep, records = run(args.root)
    if args.export:
        json.dump(export(records), sys.stdout, ensure_ascii=False, indent=1)
        print()
        return 1 if rep.gates else 0
    counts = {t: sum(r["type"] == t for r in records.values()) for t in RECORD_TYPES}
    status = "RED" if rep.gates else ("AMBER" if rep.warns else "GREEN")
    print(f"preflight: {status} — {len(rep.gates)} gate(s), {len(rep.warns)} warning(s)")
    print("RECORDS " + " · ".join(f"{t}={n}" for t, n in counts.items()))
    for line in rep.info:
        print(line)
    for tag, items in (("GATE", rep.gates), ("WARN", rep.warns)):
        for msg, remedy in items:
            print(f"{tag} {msg}\n     REMEDY: {remedy}")
    return 1 if rep.gates else 0


if __name__ == "__main__":
    sys.exit(main())
