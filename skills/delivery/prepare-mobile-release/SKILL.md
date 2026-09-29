---
name: prepare-mobile-release
description: "Prepare a coordinated consumer-mobile release across backend, app updates and native builds. Use for release readiness and authorized coordination, not generic PR review."
metadata:
  maturity: field-derived
---

# Prepare Mobile Release

Use the user's existing project context, policies and tools. Ask only for missing information that materially changes the result. Accept authorized exports when live integrations are unavailable; distinguish unavailable evidence from negative evidence. Follow the requested depth: discussion and audit do not authorize implementation or external actions. Keep project-specific data in the project rather than this public skill.

At invocation, read [the corrective-feedback loop](references/feedback-loop.md) and [regression cases](references/regression-cases.md). Apply learned corrections below before choosing an approach.

## Workflow

1. Inventory exact commits, dependent PRs, migrations, feature flags, environments and installed-client contracts. Confirm what is merged, deployed, in preview and actually released; these are distinct states.

2. Determine native-build versus over-the-air eligibility from real changed dependencies and current platform rules. Do not infer that all JavaScript changes are safe for every runtime.

3. Plan deployment order and backward compatibility. Verify old clients against the new backend, including missing fields and behavior changes. Separate reversible flags from irreversible data changes.

4. Prepare or coordinate the requested preview candidate. When combining branches, preserve owners’ work, rerun relevant checks on the combined revision and identify superseded PRs without closing incomplete requirements.

5. Bind device checks and screenshots to the exact candidate/build. Define rollout observation and recovery limits. Merge, publish or promote only within actual authorization; preparation alone is not release approval.

6. After authorized execution, verify deployed identifiers and user-visible behavior, then reconcile issue status and remaining manual gates.

## Deliverable

Dependency/release matrix, exact candidate, test/device evidence, rollout/recovery plan and execution status.

## Example request

> Use the prepare-mobile-release skill: Prepare these web and mobile changes for a verifiable preview and release.

## Learned corrections

When corrective feedback follows this skill, update the relevant instruction and its regression case in the same turn using the linked loop. Keep project-only values in private project context; keep this section limited to reusable decision rules.
