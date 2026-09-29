# Validation

## Checks included

- YAML entrypoints and optional UI metadata, matching names and catalog entries.
- Complete feedback-loop and regression references in every skill.
- Relative references remain within the individual skill; each folder is tested after an independent copy.
- Missing learning files, broken references, escaping dependencies, private local paths and invalid names are rejected by negative tests.
- A real synthetic correction is written into a disposable installed copy and remains valid after its regression case is added.
- Basic publication hygiene patterns flag private paths, personal mail addresses, production token shapes and UUID-like source identifiers. This is a screening aid, not an exhaustive secret scanner.

The initial edition also passed the Codex skill-creator frontmatter/scaffold validator for every skill. That external validator is not a runtime dependency of the collection.

## Reproduce

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

No production credentials are needed. GitHub Actions runs the repository checks on pushes and pull requests.

## Behavioral checks

Each skill has `references/regression-cases.md`: a domain failure, corrective follow-up and neighboring case. Use a writable disposable copy, invoke the skill on synthetic inputs, then give corrective feedback. Inspect the actual result, skill diff, regression update and neighboring-case behavior. Do not score success from keyword presence alone.

Manual initial review covered the workflow boundaries and the evidence/authorization rules. There has been no independent-agent benchmark or live end-to-end run of every integration. Packaging tests do not prove conversion gains, correct financial calculations, legal sufficiency, deployment safety or reliable media generation. The skills request appropriate verification during execution and label missing evidence.

An agent must have continued context and permission to edit the loaded copy for the learning loop to persist. To test read-only behavior, make a disposable copy read-only and confirm the agent returns a concrete patch and a persistence limitation rather than claiming the installed skill changed. Do not automatically publish learned changes.

Vendor metadata is optional: a test removes the adapter directory and confirms that the standalone skill remains valid. Documentation links in the root, docs and examples are checked as well.

## Installer smoke check

The visitor-packaging revision was checked with `skills` CLI 1.7.0: discovery found all 26 skills, and a project-scoped copy install of `polish-mobile-flow` targeting Claude Code, Codex and Cursor succeeded in a disposable directory. The installed copies retained the entrypoint, feedback loop and regression references. This verifies installer packaging, not agent runtime behavior or every integration.
