---
name: investigate-customer
description: "Resolve a customer\u2019s identity, billing, entitlement and activity context from authorized records. Use for an account-specific question; use journey diagnosis for reproducing app/network failures."
metadata:
  maturity: field-derived
---

# Investigate Customer

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Resolve the supplied identifier across app and billing sources. Prefer explicit account/provider mappings. Surface duplicate emails, aliases, transfers and conflicting matches; never silently choose the first result.

2. Build a timestamped account, payment, subscription, entitlement and product-activity timeline. Distinguish source records from derived conclusions and missing provider access from an empty account.

3. Compare cancellation, paid-through period, refund, trial, grace and gifted access against actual product rules. Canceled does not universally mean expired, and successful payment does not prove application access.

4. Identify the smallest supported explanation and next action. Read-only investigation does not authorize refunds, account merges, access changes or sending replies.

5. Produce an evidence-backed internal summary and optional customer reply using only information appropriate for that audience. If a correction is authorized separately, verify identity and exact target again before acting and read back the result.

## Deliverable

Resolved identifiers or ambiguity, timeline, diagnosis, missing facts, next action and optional reply draft.

## Example request

> Use the investigate-customer skill: Explain why this customer paid but cannot access the product.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
