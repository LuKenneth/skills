---
name: audit-lifecycle-messaging
description: "Audit triggered consumer-app email, push and in-app messages for eligibility, timing, useful actions and suppression. Use for a lifecycle journey audit or scoped repair."
metadata:
  maturity: initial-playbook
---

# Audit Lifecycle Messaging

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Inventory triggers, queues, templates and channels. Trace actual eligibility and suppression code, not only the marketing calendar. Separate transactional delivery from promotional communication.

2. Map each message to user state, value, timezone, frequency and destination. Inspect behavior when users subscribe, cancel, complete the action, opt out or change account state between enqueue and send.

3. Check idempotency, retry handling, stale queued messages and cross-channel duplication. Verify preferences and applicable platform requirements using current authoritative sources when relevant.

4. Validate deep links and web fallbacks on supported platforms. A learning CTA should reach its promised action; a billing CTA may appropriately remain on the web.

5. Use previews and approved test accounts for verification. Track delivery, action and product outcomes separately. Recommend a bounded repair or experiment without sending campaigns merely because an audit was requested.

## Deliverable

Trigger/state/destination map, prioritized defects, revised drafts or requested repairs, and verification evidence.

## Example request

> Use $audit-lifecycle-messaging: Audit trial reminders and re-engagement messages against actual account behavior.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
