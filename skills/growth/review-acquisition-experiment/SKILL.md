---
name: review-acquisition-experiment
description: "Evaluate a consumer-app acquisition change using spend, cohort maturity and downstream outcomes. Use for campaign readouts and next-test decisions, not automatic budget changes."
metadata:
  maturity: field-derived
---

# Review Acquisition Experiment

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Reconstruct the actual change log across all campaigns, channels, budgets, geographies and creative. Distinguish reallocating spend from increasing total spend.

2. Define exposure, acquisition cohort, attribution method and comparable windows. Allow trials to mature and separate first payments, renewals, refunds and retained revenue.

3. Reconcile ad-platform reports with product and billing evidence. Mark self-reported source, anonymous clicks and modeled attribution separately. Check overlap and identity gaps before aggregating.

4. Compare the business objective, not only cheap clicks or installs. Include costs, fees/refunds and lag relevant to the requested economics; label assumptions rather than manufacturing lifetime value.

5. Recommend hold, investigate, stop or a bounded next test with a rationale and observation condition. A before/after comparison with simultaneous changes is directional, not a clean causal experiment. Do not modify budgets unless requested.

## Deliverable

Comparable readout, assumptions and data gaps, decision options and a follow-up measurement condition.

## Example request

> Use $review-acquisition-experiment: Compare our latest acquisition change with the previous period.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
