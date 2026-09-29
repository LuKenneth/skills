---
name: review-mobile-compatibility
description: "Review cross-version API, data and release compatibility for consumer mobile changes. Use for compatibility-focused PR review, especially backend changes consumed by installed older clients."
metadata:
  maturity: field-derived
---

# Review Mobile Compatibility

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Capture PR base/head revisions, full diff and relevant contracts. Inspect actual consumer code and released version history; current mobile main alone is insufficient.

2. Trace changed fields, nullability, enums, ordering, authentication, entitlements, cache/offline formats and side effects into supported clients. Distinguish documented contracts from speculative alternate shapes.

3. Analyze deployment order, feature flags, migrations and rollback behavior. Test the supported version combinations with meaningful fixtures or actual clients when feasible.

4. Report introduced or worsened defects with the trigger, affected version, evidence and smallest repair direction. Do not demand generalized fallbacks or tests for unsupported states.

5. Keep review separate from implementation. Recheck head before publishing comments and avoid duplicate findings. Post only when requested/authorized; otherwise return a local review. Distinguish tests run, CI read and checks unavailable.

## Deliverable

Compatibility matrix, evidenced findings, validation limits and review comments when authorized.

## Example request

> Use $review-mobile-compatibility: Check whether this backend PR is safe for already-installed mobile clients.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
