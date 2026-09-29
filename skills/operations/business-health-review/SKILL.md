---
name: business-health-review
description: "Produce a source-defined operating review of a software business across comparable time windows. Use for revenue, recurring revenue, user activity and churn reporting, not company valuation."
metadata:
  maturity: field-derived
---

# Business Health Review

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Define the requested decisions, as-of time, timezone, populations and comparison periods. Use complete periods or equivalent elapsed windows, and label partial periods.

2. Confirm the source of truth and formula for each metric. Billing providers, app data and analytics answer different questions. Read existing definitions but reconcile stale documentation against implementation and user corrections.

3. Separate receipts, refunds, recurring revenue, paying accounts, active users and trial outcomes. Exclude lifetime purchases from MRR; normalize recurring intervals and currencies explicitly. Deduplicate cross-provider overlap.

4. For historical metrics, distinguish snapshots from reconstructions and current-state approximations. A last-active timestamp cannot reconstruct arbitrary past activity. Missing sources are unknown, not zero.

5. Explain material changes with evidence and uncertainty. Avoid treating immature trials, tiny-base growth or raw averages as stable trends. Prioritize decisions and anomalies over dashboard volume; preserve calculations for review.

## Deliverable

Metric table with definitions, source/as-of notes, comparable deltas, anomalies and next decisions.

## Example request

> Use $business-health-review: Review this week and month against equivalent prior periods.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
