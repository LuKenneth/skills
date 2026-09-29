---
name: diagnose-user-journey
description: "Investigate an actual customer failure across app behavior, analytics, network conditions and releases. Use for a broken user journey; use account investigation for billing/identity context alone."
metadata:
  maturity: field-derived
---

# Diagnose User Journey

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Build a timeline from the customer report, app/build version, platform, account state, network conditions and recent release history. Separate customer observations from proposed explanations.

2. Locate the exact failing stage and correlate relevant logs/events by identifiers and time. Inspect the deployed backend and the customer’s installed client; main branch alone is not proof that a fix reached them.

3. Reproduce the smallest supported scenario. Compare successful and failing conditions, such as Wi-Fi versus cellular, without inferring location or carrier from coarse analytics alone.

4. Form and test ranked hypotheses. Distinguish authentication, entitlement, permissions, connectivity, provider outage and UI state failures. Do not repeat retries that can duplicate charges or submissions.

5. Produce a minimal correction or vendor/support brief within scope, with redacted diagnostics and a concrete verification path. A recurrence after a fix should trigger rechecking the failure boundary, not automatically reapplying the same fix.

## Deliverable

Sourced timeline, confirmed or bounded diagnosis, impact, next action and optional customer/vendor reply draft.

## Example request

> Use the diagnose-user-journey skill: This user still cannot complete a voice session after our fix. Diagnose it.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
