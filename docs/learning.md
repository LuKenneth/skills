# Learning from corrective feedback

Every skill carries its own feedback-loop instructions and regression cases. After a correction, the agent should:

1. Fix the result.
2. Find the mistake in the workflow and edit the smallest relevant instruction.
3. Add a synthetic case that would catch a recurrence.
4. Check that case and a neighboring valid case.
5. Report the files changed and the verification performed.

This happens in the same corrective conversation. It is instruction-driven, not a background daemon. It requires continued task context and writable access to the actual loaded skill.

## What belongs where

Reusable judgment belongs in the skill. Project-only values, private customer context, brand preferences and access details belong in your own project. The skill can learn to consult those values without embedding them publicly. A correction should not turn a one-off preference into a universal rule.

## Installed copies, symlinks and forks

Find the path the agent actually loaded. Editing a checkout does not update a separate installed copy. Editing a shared canonical copy through a symlink can affect several agents. Keep a fork or backup if you want to preserve corrections across upstream updates, and merge incoming changes deliberately.

With a managed read-only installation, the agent should produce a concrete patch and regression example in a writable workspace and say that persistence is blocked. It must not claim the installed skill changed. Apply the patch to a writable copy to make future invocations use it.

## Share an improvement

Review the diff, replace private examples with synthetic ones, and follow [the contribution guide](../CONTRIBUTING.md). The loop never automatically commits, pushes or opens a PR. No feedback data is sent to the repository by the skill itself.
