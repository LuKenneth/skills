---
name: reconcile-delivery
description: "Reconcile backlog acceptance criteria with merged changes and actual release evidence. Use to audit or update delivery status, not infer value from PR counts."
metadata:
  maturity: field-derived
---

# Reconcile Delivery

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Inventory issue criteria, linked PRs, current branches, deployments and relevant discussions. Establish an as-of time and capture exact evidence.

2. Map each acceptance criterion to implemented behavior and verification. A merged partial PR does not complete the parent issue; a closed issue is not proof that behavior shipped.

3. Classify implemented, verified, released, partial, blocked, duplicate or obsolete according to the project’s vocabulary. Surface missing relationships and unresolved manual checks.

4. Propose precise tracker edits with evidence and remaining work. When authorized, update only verified statuses and link partial delivery without auto-closing unmet requirements.

5. Read back changes and provide a concise remaining-work view. Throughput counts describe activity, not equally sized features or customer value.

## Deliverable

Criterion-to-evidence table, proposed or verified status changes, and remaining delivery gaps.

## Example request

> Use the reconcile-delivery skill: Check which issues are actually complete after the recent merges.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
