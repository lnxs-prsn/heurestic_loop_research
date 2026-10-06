# Intent timeline — <project name>

Rules: SPEC.md HC-4..HC-8. Append-only. Agents reconstruct entries from
evidence (`status: derived`); only the owner confirms (recorded in
owner-log.md). The current intent is the newest confirmed, unsuperseded entry.

---

## INT-1 — <short title, e.g. "Origin: what the project set out to do">
kind: origin
describes: <ISO date the intent is as of>
status: derived
confirmed: none
evidence: <paths / record IDs / commits this is reconstructed from>
builds_on: none
supersedes: none
superseded_by: none

**For:** <what the project is for — one or two sentences>
**For whom:** <who benefits>
**Success looks like:** <observable outcome>
**Not:** <what it deliberately is not>
<Mark any statement without evidence as (inferred).>
