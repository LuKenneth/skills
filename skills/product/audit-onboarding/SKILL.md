---
name: audit-onboarding
description: "Audit a consumer-app onboarding journey against first value, instrumentation and observed friction. Use to diagnose or plan improvements; implementation requires an implementation request."
metadata:
  maturity: initial-playbook
---

# Audit Onboarding

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Define the audience, acquisition entry, first meaningful value and supported account states. Inspect the actual journey from fresh install and returning login, including permissions, confirmation, loading and failure paths.

2. Map each screen to its user purpose, required input, next action and event. Distinguish install, first open, account creation and onboarding completion; they are different denominators.

3. Reconcile event names and identity transitions against implementation. Segment comparable versions, platforms and acquisition cohorts. Check event loss and duplicate emissions before interpreting a drop as abandonment.

4. Rank friction by observed user impact and confidence. Separate required setup from optional personalization. Preserve recovery and accessibility; fewer screens alone does not establish better activation.

5. Propose the smallest testable change with a primary activation measure, conversion/retention guardrails, exposure definition and follow-up window. State missing evidence rather than inventing funnel counts.

## Deliverable

Journey map, sourced friction findings, instrumentation gaps and prioritized experiment briefs.

## Example request

> Use the audit-onboarding skill: Find where new users fail to reach their first useful result.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
