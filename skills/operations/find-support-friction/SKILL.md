---
name: find-support-friction
description: "Analyze a bounded set of support conversations to identify recurring product and self-service improvements. Use for patterns across customers, not resolving one account or auto-replying."
metadata:
  maturity: field-derived
---

# Find Support Friction

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Define the period, sample, channels and business question. Read representative full conversations including resolutions, not only subject lines or repeated notifications.

2. Group by underlying cause and user intent, separating product defect, unclear policy, missing self-service and feature demand. Count distinct cases/customers and disclose sampling bias.

3. Inspect the corresponding app/web paths before recommending a fix. Provider-specific cancellation or refund paths may differ; verify current official guidance when specifying instructions.

4. Link patterns to concrete journey changes, help content or instrumentation. Distinguish a frequent preventable issue from one loud request; preserve counterexamples and unresolved cases.

5. Prioritize by evidence, user harm, repetition and implementation scope. Provide acceptance criteria and a way to measure reduced repeat contact without concealing legitimate support access. Draft replies only if requested and do not send automatically.

## Deliverable

Evidence-backed themes, representative redacted examples, prioritized fixes and measurement plan.

## Example request

> Use $find-support-friction: Find recurring refund and access confusion we can prevent in the product.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
