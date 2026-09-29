# Behavioral regression cases

These are synthetic scenarios, not reports of completed live tests. Run them in a disposable workspace without live side effects. Judge the observable decision and result, not exact wording.

## Domain case

Input: The user says reward colors must match the original. A screenshot fixture uses plausible new colors while production code was unchanged.

Expected: Trace original colors through source/history, correct the fixture and recapture; do not change production semantics to match an invented mockup.

## Corrective follow-up

The user points out the failure described above after an initial result. Fix the result, strengthen the relevant instruction in this skill, and update this case. Verify a neighboring valid case still works. No automatic publication and no private data in the skill.

## Neighboring case

Repeat the request with the disputed assumption explicitly supported by reliable evidence. Use that evidence; do not turn the correction into a blanket prohibition that rejects valid work.
