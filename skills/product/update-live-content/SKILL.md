---
name: update-live-content
description: "Plan and execute requested updates to structured content in a live consumer product while preserving progress and references. Use for lessons, workouts, prompts or similar content catalogs."
metadata:
  maturity: field-derived
---

# Update Live Content

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Inspect identifiers, ordering, progress, recommendations, unlocks, localization and cached/offline consumers. Determine whether inserting content changes meaning for people already beyond that position.

2. Compare the proposed content with source material and editorial standards. Keep stable IDs separate from display numbering. Identify dependencies and content already delivered to users.

3. Prepare a before/after mapping and idempotent import or migration when requested. Check referential integrity, duplicate keys, ordering collisions, completion/reward behavior and old-client contracts.

4. Validate on a disposable dataset representing new, in-progress and advanced users. Define backup and rollback limits; a content reorder may not safely undo already-earned progress.

5. Apply production changes only within explicit authorization. Verify counts and relationships after execution, then align relevant reference documents and caches. Report subject-matter review still needed.

## Deliverable

Content diff, impact matrix, validated import/migration materials and documentation updates; execution receipts if authorized.

## Example request

> Use the update-live-content skill: Insert new lessons in the middle of the catalog without disrupting existing users.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
