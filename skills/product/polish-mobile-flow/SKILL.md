---
name: polish-mobile-flow
description: "Improve an existing mobile flow from user feedback and inspected design references, with verified before-and-after evidence. Use for scoped UI audits or implementation, not a new brand identity."
metadata:
  maturity: field-derived
---

# Polish Mobile Flow

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Classify the request as discussion, audit or implementation. Read the current flow, brand tokens, navigation, API states and released behavior before suggesting changes. Convert feedback into observable requirements and preserved behavior.

2. Inspect actual reference images, not search titles. Identify which pattern solves each requirement and which existing brand elements must remain. Find original values in source/history when the user asks to restore them.

3. Implement only the requested scope using production components. Fixtures must reflect real response contracts, state colors and accessibility settings. Record synthetic-data limitations.

4. Freeze the candidate before capture. Compare baseline and candidate with matching devices, text sizes and data. Check empty, loading, error, completed and mixed states as relevant, scroll reachability, safe areas and real navigation.

5. Inspect every delivered image; fix defects and recapture affected states. Run focused behavior tests. Identify the exact candidate and separate simulator evidence from outstanding real-device checks.

## Deliverable

A requirement-to-evidence table, reviewed captures, scoped change or PR when requested, and remaining verification limits.

## Example request

> Use the polish-mobile-flow skill: Improve this lesson-completion flow while preserving its reward semantics.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
