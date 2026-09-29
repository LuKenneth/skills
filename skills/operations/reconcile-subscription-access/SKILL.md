---
name: reconcile-subscription-access
description: "Audit a cohort for mismatches between billing state and product entitlement. Use for batch subscription/access reconciliation; use investigate-customer for one account."
metadata:
  maturity: initial-playbook
---

# Reconcile Subscription Access

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Define the cohort, snapshot time, environment and intended entitlement policy. Inspect provider identifiers, app mappings, period boundaries and supported exceptions.

2. Fetch read-only billing and application snapshots with timestamps and pagination. Deduplicate transfers, aliases and overlapping providers; do not treat inaccessible records as inactive subscriptions.

3. Classify mismatches into paid-without-access, expired-with-access, delayed sync, intentional exception and unresolved identity. Account for paid-through cancellations, grace, lifetime, gifts and refunds according to policy.

4. Produce per-record evidence and aggregate counts with the same denominator. Investigate representative mismatches before proposing a batch action; a stale replica may explain the whole group.

5. Prepare a narrowly scoped repair plan with preconditions, dry-run targets, rollback limits and verification. Do not run production repairs unless authorized; revalidate targets at execution time.

## Deliverable

Mismatch report, exceptions, source freshness, proposed repairs and verification criteria.

## Example request

> Use the reconcile-subscription-access skill: Find paid customers missing access and expired accounts retaining access.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
