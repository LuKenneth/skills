# Contributing

Start with a demonstrated failure or a workflow you actually use. Open an issue describing the input, expected result and observed failure, or submit a small PR with a synthetic regression case.

## Keep the collection portable

- Keep core instructions in `SKILL.md` and local references. Agent-specific UI metadata is optional.
- Use ordinary language for invocations and tool capabilities. Do not require a vendor SDK, proprietary connector or sibling skill unless the workflow truly needs it.
- Preserve public skill names and category paths where possible. Update the catalog and documentation when metadata changes.
- Include each skill's local feedback loop and regression cases. Keep the folders independently installable.
- Never add customer exports, credentials or private project policies. Use synthetic examples.

## Check a change

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

Try the corrected scenario and a neighboring valid case with an agent. Describe what you actually ran and any limitations; packaging tests cannot establish decision quality. For installer changes, also check discovery and a project-scoped install in a disposable directory.

If your correction changes a description or maturity field, update `catalog.json`. If it changes who should use a skill, update `docs/skills.md`. [Validation details](docs/validation.md) explain the checks and limits.
