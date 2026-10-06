#!/usr/bin/env python3
"""Self-tests for preflight (specs/08 BP-19): every planted defect is caught.

    python3 scripts/test_preflight.py
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import preflight  # noqa: E402

DECISION = """## D-{n} — Title {n}
status: accepted
date: 2026-07-10T20:00+03:00
decided_by: owner
supersedes: {sup}
superseded_by: {sby}
affects: BP-1
evidence: BUILDLOG@2026-07-10T20:00+03:00
"""

PROPOSAL = """## D-{n} — Open question
status: proposed
date: 2026-07-10T20:00+03:00
decided_by: pending
supersedes: none
superseded_by: none
affects: P1.1
evidence: BUILDLOG@2026-07-10T20:00+03:00

Options:
  A) yes   ← DEFAULT
  B) no
Decision: pending
"""

INTAKE = """# INDEX

## I-1 — a.md
status: unread
date: 2026-09-08
received: 2026-10-05
source: owner
file: insights_from_other_conversations/a.md
affects: D-1
evidence: BUILDLOG@2026-07-10T20:00+03:00
"""

BUILDLOG = """# BUILDLOG

## 2026-07-10T20:00+03:00 · agent · pi · scope
INTENT: something; cites D-1.
"""


class Fixture:
    """A minimal, valid repo; tests mutate one thing each."""

    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.write("specs/01-invariants.md", "- **BP-1** a rule\n")
        self.write("specs/06-phases.md", "| P1.1 | scaffold | — | — |\n")
        self.write("progress/BUILDLOG.md", BUILDLOG)
        self.write("progress/decisions.md",
                   "# decisions\n\n" + DECISION.format(n=1, sup="none", sby="none"))
        self.write("insights_from_other_conversations/INDEX.md", INTAKE)
        self.write("insights_from_other_conversations/a.md", "x\n")
        self.write("progress/STATUS.md", "# STATUS\npending_decisions: none\n")
        g = ["git", "-C", str(self.root), "-c", "user.name=t", "-c", "user.email=t@t"]
        subprocess.run(g[:3] + ["init", "-q"], check=True)
        subprocess.run(g + ["add", "."], check=True)
        subprocess.run(g + ["commit", "-qm", "init"], check=True)
        sha = subprocess.run(g[:3] + ["rev-parse", "--short", "HEAD"], check=True,
                             capture_output=True, text=True).stdout.strip()
        self.handoff(as_of="2026-07-10T20:00+03:00", sha=sha, body="see D-1")
        self.sha = sha

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def append(self, rel, text):
        with open(self.root / rel, "a", encoding="utf-8") as fh:
            fh.write(text)

    def handoff(self, as_of, sha, body, pending="none"):
        self.write("progress/HANDOFF.md",
                   f"# HANDOFF\nas_of: {as_of}\nverified_at: {sha}\n"
                   f"pending_decisions: {pending}\n\n{body}\n")

    def set_pending(self, pending):
        self.handoff("2026-07-10T20:00+03:00", self.sha, "see D-1", pending)
        self.write("progress/STATUS.md", f"# STATUS\npending_decisions: {pending}\n")

    def run(self):
        rep, _ = preflight.run(self.root)
        return [m for m, _ in rep.gates], [m for m, _ in rep.warns]


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.fx = Fixture()
        self.addCleanup(self.fx.tmp.cleanup)

    def assertCaught(self, msgs, needle):
        self.assertTrue(any(needle in m for m in msgs), f"{needle!r} not in {msgs}")

    def test_clean_fixture_has_no_gates(self):
        gates, _ = self.fx.run()
        self.assertEqual(gates, [])

    def test_dangling_reference(self):
        self.fx.append("progress/decisions.md",
                       DECISION.format(n=2, sup="none", sby="none")
                       .replace("affects: BP-1", "affects: BP-99"))
        self.assertCaught(self.fx.run()[0], "'BP-99' does not resolve")

    def test_missing_field(self):
        self.fx.append("progress/decisions.md",
                       DECISION.format(n=2, sup="none", sby="none")
                       .replace("decided_by: owner\n", ""))
        self.assertCaught(self.fx.run()[0], "missing field 'decided_by'")

    def test_duplicate_id(self):
        self.fx.append("progress/decisions.md",
                       DECISION.format(n=1, sup="none", sby="none"))
        self.assertCaught(self.fx.run()[0], "duplicate id D-1")

    def test_proposal_without_default(self):
        self.fx.append("progress/decisions.md",
                       PROPOSAL.format(n=2).replace("   ← DEFAULT", ""))
        self.assertCaught(self.fx.run()[0], "lacks '← DEFAULT'")

    def test_valid_proposal_only_warns(self):
        self.fx.append("progress/decisions.md", PROPOSAL.format(n=2))
        self.fx.set_pending("D-2")
        gates, warns = self.fx.run()
        self.assertEqual(gates, [])
        self.assertCaught(warns, "D-2 awaits owner")

    def test_stale_pending_claim(self):
        # GOLD-6 case: a decision listed as pending after the owner answered it
        self.fx.set_pending("D-1")
        self.assertCaught(self.fx.run()[0], "lists D-1 as pending, but the ledger")

    def test_unmentioned_pending_decision(self):
        self.fx.append("progress/decisions.md", PROPOSAL.format(n=2))
        self.assertCaught(self.fx.run()[0], "omits pending decision D-2")

    def test_pending_line_required(self):
        self.fx.write("progress/STATUS.md", "# STATUS\n")
        self.assertCaught(self.fx.run()[0], "needs exactly 1")

    def test_supersede_must_be_symmetric(self):
        self.fx.append("progress/decisions.md",
                       DECISION.format(n=2, sup="D-1", sby="none"))
        self.assertCaught(self.fx.run()[0], "D-1.superseded_by lacks D-2")

    def test_unparseable_buildlog_heading(self):
        self.fx.append("progress/BUILDLOG.md", "\n## yesterday · agent\n")
        self.assertCaught(self.fx.run()[0], "unparseable record heading")

    def test_unregistered_intake_file(self):
        self.fx.write("insights_from_other_conversations/new.md", "x\n")
        self.assertCaught(self.fx.run()[1], "unregistered intake file")

    def test_intake_file_missing(self):
        (self.fx.root / "insights_from_other_conversations/a.md").unlink()
        self.assertCaught(self.fx.run()[0], "does not exist")

    def test_handoff_cites_unknown_decision(self):
        self.fx.handoff("2026-07-10T20:00+03:00", self.fx.sha, "see D-99")
        self.assertCaught(self.fx.run()[0], "cites 'D-99'")

    def test_handoff_older_than_buildlog(self):
        self.fx.append("progress/BUILDLOG.md",
                       "\n## 2026-07-11T09:00+03:00 · agent · pi · later\nx\n")
        self.assertCaught(self.fx.run()[1], "is older than newest BUILDLOG entry")

    def test_handoff_without_fields(self):
        self.fx.write("progress/HANDOFF.md", "# HANDOFF\nno fields\n")
        gates, _ = self.fx.run()
        self.assertCaught(gates, "lacks a valid 'as_of:'")
        self.assertCaught(gates, "lacks a valid 'verified_at:'")

    def test_export_has_typed_edges(self):
        _, records = preflight.run(self.fx.root)
        edges = preflight.export(records)["edges"]
        self.assertIn({"src": "D-1", "rel": "affects", "dst": "BP-1"}, edges)
        self.assertIn({"src": "BUILDLOG@2026-07-10T20:00+03:00",
                       "rel": "mentions", "dst": "D-1"}, edges)


if __name__ == "__main__":
    unittest.main()
