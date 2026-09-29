---
name: prepare-dispute-evidence
description: "Prepare a factual subscription or digital-product payment dispute response and evidence packet. Use for evidence preparation, not automatic submission or claims of guaranteed outcomes."
metadata:
  maturity: field-derived
---

# Prepare Dispute Evidence

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Identify the disputed transaction, provider, amount, reason, deadline and customer linkage. Use current official provider requirements when deciding submission fields or limits. Do not confuse unrelated subscriptions with the disputed charge.

2. Collect relevant authorized billing, terms/consent, fulfillment, product usage and correspondence evidence. Preserve timestamps and sources, relevant contrary evidence and gaps. A current terms page is not proof of what was accepted earlier.

3. Distinguish activity before versus after the payment. Queued email is not delivered email; analytics activity is not proof of identity; coarse geolocation is not GPS. Missing analytics must not become a fabricated device claim.

4. Build a concise merchant response addressing the actual reason. Separate a minimized submission packet from private working JSON and diagnostics. Omit redundant provider screenshots unless they add necessary context.

5. Render the requested PDF or suitable attachment, inspect every page and verify IDs, amounts, dates, readability and citations. Package only relevant supporting material, label unavailable evidence and preserve the draft. Submit only when explicitly authorized.

## Deliverable

Submission-ready evidence document, response draft, source index, private working evidence kept separate, and material limitations.

## Example request

> Use $prepare-dispute-evidence: Prepare a dispute response from this payment, usage and support evidence.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
