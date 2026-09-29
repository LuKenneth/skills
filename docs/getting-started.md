# Getting started

## Install a few skills

From your application or working project directory:

```sh
npx skills@latest add lukenneth/skills
```

The installer lets you select skills, agents and installation options. Start small. To preview the catalog without installing:

```sh
npx skills@latest add lukenneth/skills --list
```

Select one skill or target one supported agent:

```sh
npx skills@latest add lukenneth/skills --skill investigate-customer
npx skills@latest add lukenneth/skills --skill polish-mobile-flow --agent claude-code
npx skills@latest add lukenneth/skills --skill polish-mobile-flow --agent codex
npx skills@latest add lukenneth/skills --skill polish-mobile-flow --agent cursor
```

Omit `--agent` to choose interactively. Project installation is the default; use `--global` if you deliberately want a personal installation across projects. Avoid installing duplicate global/project copies without understanding which your agent loads. Installer behavior is documented in the [upstream CLI](https://github.com/vercel-labs/skills).

## Agents and invocation

The same skill files work with agents that support the Agent Skills format. Installation support does not imply that each agent's tools can complete every task.

| Environment | Invocation |
| --- | --- |
| Any capable agent | Ask it to use the named skill and supply the task/context |
| Agents with a skill picker or slash commands | Select the installed skill using the host's UI |
| Codex | The optional UI metadata includes a `$skill-name` prompt |
| Agent without skill discovery | Ask it to read the chosen `SKILL.md` and linked local references |

Core instructions do not depend on a proprietary API, a particular tool name or another installed skill. The `agents/openai.yaml` files are optional UI adapters. Automatic discovery and command syntax are host-specific; this repository does not promise identical behavior in every agent.

## Give it enough context

Supply the task, intended audience, actual source material and relevant business rules. Existing project docs are fine. If needed, copy [the operator context template](../examples/operator-context.md) into your private project.

Start with a reviewable task, for example:

> Use refresh-social-proof. Here are twelve exported store reviews and our onboarding screenshots. Recommend three exact excerpts and explain where each belongs. Prepare drafts only.

Exports and files work when live integrations are unavailable. Do not paste credentials into skill files. A skill is a workflow, not a permission grant to publish, message customers or change billing.

## Manual installation without Node.js

Clone or download the repository. Copy the whole selected skill folder into your agent's supported skill directory. Keep `SKILL.md` and `references/` together; `agents/` is optional metadata.

```sh
git clone https://github.com/lukenneth/skills.git consumer-operator-skills
```

For example, to install a personal Claude Code skill:

```sh
mkdir -p ~/.claude/skills
cp -R consumer-operator-skills/skills/product/polish-mobile-flow ~/.claude/skills/
```

For a personal Codex skill:

```sh
mkdir -p ~/.codex/skills
cp -R consumer-operator-skills/skills/product/polish-mobile-flow ~/.codex/skills/
```

Inspect existing same-named installations before copying. No whole-repo installation or project setup skill is required.

## Updates and local learning

For installer-managed copies, the CLI offers:

```sh
npx skills@latest update
```

Before updating, save local corrections in a fork or backup and compare incoming changes. Updates/reinstallation may replace local edits. Shared symlinks can share changes between agents; independent copies can diverge. Choose the arrangement intentionally. Manual installs require manually comparing and copying updates.

[Learning, read-only installations and contributing corrections →](learning.md)
