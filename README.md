# Skills for Consumer Software Operators

Practical agent skills for the work around a consumer app: improving the product, finding customers, shipping updates, and keeping the business running.

Created by [Luke Patterson](https://github.com/LuKenneth) from operating consumer software. Start with one skill, bring your own tools and project context, and adapt it as you work. Each skill learns from your corrective feedback by updating its local instructions.

## Get started

Run this from the project where you want to use the skills:

```sh
npx skills@latest add lukenneth/skills
```

Choose the skills and agents you want. The [open skills installer](https://github.com/vercel-labs/skills) supports Claude Code, Codex, Cursor, OpenCode and other agents. You need Node.js for this installation method; the skills themselves are Markdown instructions.

Or start with a single skill:

```sh
npx skills@latest add lukenneth/skills --skill polish-mobile-flow
```

Then ask your agent:

> Use the polish-mobile-flow skill to improve this completion screen. Preserve reward behavior and show verified before-and-after screenshots.

No required setup interview, custom MCP server or vendor SDK. Bring screenshots, source files, exports or connected tools relevant to the job. [Installation, manual setup and updates →](docs/getting-started.md)

## What do you need to do?

| Situation | Start with | What you get |
| --- | --- | --- |
| The app works, but the flow feels rough | [polish-mobile-flow](skills/product/polish-mobile-flow/SKILL.md) | A scoped improvement with visual verification |
| Good reviews are scattered across the stores | [refresh-social-proof](skills/growth/refresh-social-proof/SKILL.md) | Sourced reviews adapted to your paywall, onboarding and site |
| You want a useful free resource that leads into the app | [build-lead-magnet-funnel](skills/growth/build-lead-magnet-funnel/SKILL.md) | Resource, capture, delivery and a relevant next step |
| You have footage but no coherent campaign | [assets-to-campaign](skills/creative/assets-to-campaign/SKILL.md) | Story concepts, drafts, captions and an editing-review flow |
| A customer paid but cannot get access | [investigate-customer](skills/operations/investigate-customer/SKILL.md) | A reconciled account timeline and next action |
| Backend and mobile changes need to ship together | [prepare-mobile-release](skills/delivery/prepare-mobile-release/SKILL.md) | Compatibility checks, release order and a verified candidate |

## Browse all 26 skills

| Collection | Skills | Focus |
| --- | ---: | --- |
| [Product](docs/skills.md#product) | 6 | Onboarding, paywalls, retention, content and user journeys |
| [Growth](docs/skills.md#growth) | 6 | Social proof, lead magnets, brand rollout and acquisition |
| [Creative](docs/skills.md#creative) | 4 | Campaigns, hook experiments, stories and scripts |
| [Operations](docs/skills.md#operations) | 7 | Customers, disputes, metrics, alerts and contractor delivery |
| [Delivery](docs/skills.md#delivery) | 3 | Releases, compatibility and delivery status |

[Full catalog with example requests →](docs/skills.md)

## Combine them when the job needs it

- **Improve activation:** audit-onboarding → polish-mobile-flow → prepare-mobile-release.
- **Turn a story into a creative test:** journal-to-video → hook-engine → test-creative-hooks.
- **Learn from customer problems:** find-support-friction → diagnose-user-journey → reconcile-delivery.

Each skill works alone. These are suggested handoffs, not an orchestrator that runs or grants permission for the next step. [Worked examples →](examples/workflows.md)

## Use your agent and your stack

The portable interface is `SKILL.md` plus its local references, following the [Agent Skills format](https://agentskills.io/specification). No particular model, billing platform, database or analytics provider is required. Optional `agents/openai.yaml` files provide Codex UI hints; other agents can ignore them.

An agent still needs the capabilities required by the task: a PDF renderer for a PDF, access to code for implementation, or authorized billing data for a dispute. Missing tools are reported as limits. [Compatibility and invocation →](docs/getting-started.md#agents-and-invocation)

## Make them yours

When you correct a result, the skill instructs the agent to fix it, update the relevant instruction, and add a regression example. This needs writable skill files and an agent that follows the feedback instructions. Private project preferences stay in your project; corrections are never automatically pushed upstream.

Keep a fork or backup of local improvements before updating. [How feedback and updates work →](docs/learning.md)

## About this collection

This is an initial public collection. The [catalog](docs/skills.md) distinguishes workflows derived from operating experience from newer playbooks. Packaging checks pass; that is not a claim that every workflow has been benchmarked across every agent. [Validation details →](docs/validation.md)

Inspired by the practical, composable packaging of [Matt Pocock's skills](https://github.com/mattpocock/skills). These workflows focus on operating consumer software.

[Contribute](CONTRIBUTING.md) · [Report an issue](https://github.com/LuKenneth/skills/issues) · [MIT license](LICENSE)
