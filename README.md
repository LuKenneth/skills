# Skills for consumer software operators

Agent workflows for building, growing and running consumer apps. Built from real operating patterns, with portable project context and a corrective-feedback loop in every skill.

These are editable instructions, not a hosted service or an autonomous workforce. They help an agent finish a defined job using the tools and access you provide. No subscription or proprietary connector is required by the instructions; individual jobs may need billing exports, source code, analytics, a browser, media tooling or a connected account.

## Start here

Try **polish-mobile-flow**, **refresh-social-proof**, **build-lead-magnet-funnel**, or **assets-to-campaign**. Choose one workflow and supply the relevant project context. Install only what you need.

## Install

Clone this repository, then copy a complete skill folder (including `references` and `agents`) into your agent's skills directory. For Codex, a personal installation is typically `~/.codex/skills/<skill-name>/`. Other agents can use their own supported skill location or read the entrypoint directly. Category folders organize this repository; each individual skill is self-contained.

```sh
git clone https://github.com/lukenneth/skills.git
mkdir -p ~/.codex/skills
cp -R skills/skills/product/polish-mobile-flow ~/.codex/skills/
```

Use a writable copy if you want corrective feedback to persist. Existing same-named skills should be compared before replacement; do not overwrite your own changes blindly.

Example: `Use $polish-mobile-flow to improve this completion screen. Preserve reward behavior and include verified before/after screenshots.`

## The collection

### Product

| Skill | Job |
| --- | --- |
| [polish-mobile-flow](skills/product/polish-mobile-flow/SKILL.md) | Improve an existing mobile flow from user feedback and inspected design references, with verified before-and-after evidence. |
| [audit-onboarding](skills/product/audit-onboarding/SKILL.md) | Audit a consumer-app onboarding journey against first value, instrumentation and observed friction. |
| [review-paywall](skills/product/review-paywall/SKILL.md) | Review consumer subscription paywalls and offer presentation using actual product, billing and entitlement rules. |
| [plan-retention-experiment](skills/product/plan-retention-experiment/SKILL.md) | Design a measurable consumer-app retention experiment from behavior and customer evidence. |
| [update-live-content](skills/product/update-live-content/SKILL.md) | Plan and execute requested updates to structured content in a live consumer product while preserving progress and references. |
| [diagnose-user-journey](skills/product/diagnose-user-journey/SKILL.md) | Investigate an actual customer failure across app behavior, analytics, network conditions and releases. |

### Growth

| Skill | Job |
| --- | --- |
| [refresh-social-proof](skills/growth/refresh-social-proof/SKILL.md) | Refresh customer reviews and testimonials across specified consumer-app surfaces with source attribution and accurate excerpts. |
| [build-lead-magnet-funnel](skills/growth/build-lead-magnet-funnel/SKILL.md) | Build or improve a consumer-product lead-magnet journey connecting a useful resource, capture, delivery and a relevant product next step. |
| [roll-out-brand-update](skills/growth/roll-out-brand-update/SKILL.md) | Apply an approved brand direction consistently across specified consumer-product touchpoints. |
| [prepare-growth-brief](skills/growth/prepare-growth-brief/SKILL.md) | Assemble a dated, evidence-backed consumer-app growth packet for an advisor or collaborator. |
| [review-acquisition-experiment](skills/growth/review-acquisition-experiment/SKILL.md) | Evaluate a consumer-app acquisition change using spend, cohort maturity and downstream outcomes. |
| [audit-lifecycle-messaging](skills/growth/audit-lifecycle-messaging/SKILL.md) | Audit triggered consumer-app email, push and in-app messages for eligibility, timing, useful actions and suppression. |

### Creative

| Skill | Job |
| --- | --- |
| [assets-to-campaign](skills/creative/assets-to-campaign/SKILL.md) | Turn existing footage, interviews or UGC into source-backed campaign concepts and reviewable posts. |
| [test-creative-hooks](skills/creative/test-creative-hooks/SKILL.md) | Produce and evaluate controlled hook variants for an existing creative asset. |
| [hook-engine](skills/creative/hook-engine/SKILL.md) | Improve truthful video hooks, openings and retention structure from supplied source material or an existing script. |
| [journal-to-video](skills/creative/journal-to-video/SKILL.md) | Extract source-grounded video concepts and requested scripts from journals, voice notes or unstructured founder reflections. |

### Operations

| Skill | Job |
| --- | --- |
| [investigate-customer](skills/operations/investigate-customer/SKILL.md) | Resolve a customer’s identity, billing, entitlement and activity context from authorized records. |
| [reconcile-subscription-access](skills/operations/reconcile-subscription-access/SKILL.md) | Audit a cohort for mismatches between billing state and product entitlement. |
| [prepare-dispute-evidence](skills/operations/prepare-dispute-evidence/SKILL.md) | Prepare a factual subscription or digital-product payment dispute response and evidence packet. |
| [business-health-review](skills/operations/business-health-review/SKILL.md) | Produce a source-defined operating review of a software business across comparable time windows. |
| [triage-production-alerts](skills/operations/triage-production-alerts/SKILL.md) | Triage a bounded batch of production alerts and related support signals into actionable incidents. |
| [find-support-friction](skills/operations/find-support-friction/SKILL.md) | Analyze a bounded set of support conversations to identify recurring product and self-service improvements. |
| [review-contractor-delivery](skills/operations/review-contractor-delivery/SKILL.md) | Review agreed contractor output against scope, quality, time and dependencies. |

### Delivery

| Skill | Job |
| --- | --- |
| [prepare-mobile-release](skills/delivery/prepare-mobile-release/SKILL.md) | Prepare a coordinated consumer-mobile release across backend, app updates and native builds. |
| [reconcile-delivery](skills/delivery/reconcile-delivery/SKILL.md) | Reconcile backlog acceptance criteria with merged changes and actual release evidence. |
| [review-mobile-compatibility](skills/delivery/review-mobile-compatibility/SKILL.md) | Review cross-version API, data and release compatibility for consumer mobile changes. |

## Project context

Keep the business-specific information in your own project. Start with [the context template](examples/operator-context.md), or use existing docs. Skills do not assume a particular schema, platform, brand or permission model. Provide references to credentials, never their values in context documents.

Common distinctions: `investigate-customer` resolves one account; `reconcile-subscription-access` audits a cohort; `diagnose-user-journey` traces a product failure. `hook-engine` improves the idea/opening; `test-creative-hooks` controls a variant experiment; `assets-to-campaign` produces a broader batch. `review-mobile-compatibility` reviews contracts; `prepare-mobile-release` coordinates a release; `reconcile-delivery` reconciles accepted work with actual delivery.

## Learning from corrections

Every skill includes its own feedback-loop instructions. When you correct a result, the executing agent is instructed to fix the result, edit the relevant skill instruction, add a synthetic regression case, check that correction and a neighboring case, and tell you what changed. Project-only preferences stay in your private context; the reusable skill learns to consult them.

This requires an agent with writable access to the loaded skill and continued context from your correction. It is not an automatic background process. Read-only installations produce a proposed patch and an explicit persistence limitation. Local corrections are never automatically published to this repository. Review and sanitize changes before contributing them.

## Maturity and validation

All skills are an initial public edition. `field-derived` means the workflow was extracted from operating patterns; it does not mean independently benchmarked. `initial-playbook` marks adjacent recommendations that need more real-world iteration. See [the catalog](catalog.json) for each label.

Each skill includes synthetic behavioral cases. Repository checks validate packaging and privacy patterns; they do not prove that an agent will make the correct business decision or that every integration works. See [validation](VALIDATION.md) for the release checks and limits.

Install development dependencies with `python3 -m pip install -r requirements-dev.txt` in a virtual environment, then run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests` before contributing. Add a case for the failure your change prevents. Avoid blanket policies from one example, new tool dependencies without a concrete need, or generic instructions that do not change a decision.

## Origins and scope

Created by Luke Patterson for independent consumer-software operators. Inspired by the clear task packaging in [Matt Pocock's skills](https://github.com/mattpocock/skills); this collection focuses on operating consumer products. Public examples are synthetic. No customer records, private conversation exports or paid third-party playbooks are included.

See [coverage](COVERAGE.md) for how the recommended workflows map to the collection.

## License

MIT. See [LICENSE](LICENSE).
