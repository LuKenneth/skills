---
name: plan-retention-experiment
description: "Design a measurable consumer-app retention experiment from behavior and customer evidence. Use for a bounded hypothesis and test plan, not generic engagement tactics."
metadata:
  maturity: initial-playbook
---

# Plan Retention Experiment

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Define the returning behavior that reflects product value, cohort entry, eligible population and observation window. Distinguish habit, notification opens and successful use.

2. Inspect qualitative reasons and behavior around the drop. Separate users who never activated from activated users who stopped; segment only when the evidence supports it.

3. Choose one mechanism addressing the evidenced cause, such as a clearer next step, saved progress or a timely reminder. Explain why it could help and what would falsify it.

4. Define exposure, assignment unit, holdout when feasible, primary outcome, guardrails, minimum observation window and stopping conditions. Avoid cross-device contamination and treating repeated looks as independent tests.

5. If using messages, account for permission, preferences, local time, frequency, suppression and users who already completed the action. Plan implementation and readout without enrolling or messaging users unless authorized.

## Deliverable

An experiment brief with hypothesis, eligibility, variants, instrumentation, decision criteria and limitations.

## Example request

> Use $plan-retention-experiment: Design an experiment to help activated users return for a second useful session.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
