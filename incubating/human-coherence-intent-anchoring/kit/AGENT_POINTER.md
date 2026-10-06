# Snippet for the agent entry file (AGENTS.md / CLAUDE.md / ...)

Paste under the project's agent rules (SPEC.md HC-32):

---

**Human coherence (`<cdir>/`, rules in SPEC.md).** The owner is not a file
you can re-read; keep them in step with the project's intent.
- Everything you put to the owner carries `stage`, `impact`
  (changes-intent / advances / route-only / untouched) and a one-line `why`
  in plain words, biggest impact first (HC-12..HC-15).
- Before asking the owner anything, check whether their earlier answers
  already decide it; if so, apply it and say which answer settled it (HC-29).
- Watch for coherence signals (owner contradicts the intent, can't place a
  decision, unprocessed intent-changing inbox items, busy-but-not-moving,
  long gap) and offer a re-entry; never force one (HC-28).
- Never present a derived intent as confirmed (HC-7). Never ask the owner to
  restate the project: draft it from evidence for the owner to confirm
  (HC-24). Involve the owner only on a significant intent change, a deviated
  road, or what the evidence can't settle (HC-39).
- Before calling anything a conflict, test whether one is the material or
  precondition of the other, or the difference is only wording (HC-23).
- Session opening: on a long gap or unread outside material, offer the
  re-entry frame first, before any question (HC-41). Read every timestamp
  from the clock (HC-40).
- New outside material: register it in `<cdir>/inbox/INDEX.md` the session
  you first see it (HC-16).
