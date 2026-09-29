---
name: review-paywall
description: "Review consumer subscription paywalls and offer presentation using actual product, billing and entitlement rules. Use for a paywall audit or scoped change, not general pricing valuation."
metadata:
  maturity: initial-playbook
---

# Review Paywall

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Capture each entry point, platform, locale, eligibility state and actual offer configuration. Read current provider documentation when platform behavior or purchase requirements affect the recommendation.

2. Reconcile visible price, billing interval, introductory period, renewal terms, discount duration and entitlement with provider configuration. Check restore, existing subscribers, trial-ineligible users, canceled-but-active users and purchase failures.

3. Inspect proof, benefit hierarchy and next action on the rendered screen. Separate an unclear offer from a technical purchase failure. Do not hide terms or make cancellation/restoration harder to inflate conversion.

4. Use exposure-based cohorts with comparable trial maturity. Separate paywall views, trial starts, first payments, refunds and retained revenue. No purchase attribution from unrelated aggregate totals.

5. Recommend or implement only the requested changes. Verify configured draft and published state separately; capture device evidence and remaining purchase-sandbox checks. Record a test hypothesis rather than promising conversion lift.

## Deliverable

Offer/entitlement matrix, concrete defects, proposed revisions and a measurable validation plan.

## Example request

> Use $review-paywall: Review this paywall for offer clarity and purchase-flow failures.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
