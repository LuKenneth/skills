#!/usr/bin/env python3
"""Validate portable skill packaging, YAML, relative references and publication hygiene."""
from pathlib import Path
import json
import re
import sys
import yaml

PRIVATE_PATTERNS = [r'/Users/[^/\s]+/', r'(?i)[\w.+-]+@(gmail\.com|privaterelay\.appleid\.com)', r'\b(?:ghp_|gho_|sk_live_|rk_live_)[A-Za-z0-9]{12,}', r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b']

def validate_skill(folder):
    folder = Path(folder).resolve()
    errors = []
    entry = folder / 'SKILL.md'
    if not entry.is_file():
        return ['missing SKILL.md']
    text = entry.read_text()
    match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not match:
        return ['missing YAML frontmatter']
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return [f'invalid YAML: {exc}']
    if not isinstance(meta, dict):
        return ['frontmatter must be a mapping']
    name = meta.get('name', '')
    if not isinstance(name, str) or name != folder.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        errors.append('invalid or mismatched skill name')
    desc = meta.get('description')
    if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
        errors.append('invalid description')
    for required in ['references/feedback-loop.md', 'references/regression-cases.md', 'agents/openai.yaml']:
        if not (folder / required).is_file():
            errors.append(f'missing {required}')
    for doc in folder.rglob('*.md'):
        contents = doc.read_text()
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', contents):
            if re.match(r'https?://', target):
                continue
            target = target.split('#', 1)[0]
            if not target:
                continue
            resolved = (doc.parent / target).resolve()
            if not resolved.is_relative_to(folder):
                errors.append(f'{doc.name}: reference escapes individual skill: {target}')
            elif not resolved.exists():
                errors.append(f'{doc.name}: missing reference: {target}')
        if re.search(r'\[TODO:|\bPLACEHOLDER\b', contents):
            errors.append(f'{doc.name}: unfinished scaffold')
        for pattern in PRIVATE_PATTERNS:
            if re.search(pattern, contents):
                errors.append(f'{doc.name}: possible private data; inspect before publishing')
    ui_file = folder / 'agents/openai.yaml'
    if ui_file.exists():
        try:
            ui = yaml.safe_load(ui_file.read_text())['interface']
            if not 25 <= len(ui['short_description']) <= 64:
                errors.append('UI short description must be 25–64 characters')
            if '$' + name not in ui['default_prompt']:
                errors.append('UI prompt must invoke this skill')
        except (yaml.YAMLError, KeyError, TypeError):
            errors.append('invalid UI metadata')
    return errors

def validate_repo(root):
    root = Path(root).resolve()
    errors = []
    catalog = json.loads((root / 'catalog.json').read_text())
    names = [row['name'] for row in catalog]
    if len(set(names)) != len(names):
        errors.append('duplicate catalog entries')
    actual = {str(p.parent.relative_to(root)) for p in (root / 'skills').glob('*/*/SKILL.md')}
    expected = {f"skills/{r['group']}/{r['name']}" for r in catalog}
    if actual != expected:
        errors.append(f'catalog/files mismatch: {actual ^ expected}')
    for row in catalog:
        folder = root / 'skills' / row['group'] / row['name']
        errors.extend(f"{row['name']}: {e}" for e in validate_skill(folder))
        if (folder / 'SKILL.md').exists():
            meta = yaml.safe_load((folder / 'SKILL.md').read_text().split('---', 2)[1])
            if meta.get('description') != row['description'] or meta.get('metadata', {}).get('maturity') != row['maturity']:
                errors.append(f"{row['name']}: stale catalog metadata")
    for doc in root.glob('*.md'):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
            if not re.match(r'https?://', target) and not (root / target.split('#')[0]).exists():
                errors.append(f'{doc.name}: missing link: {target}')
    return errors

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    errors = validate_repo(root)
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print(f"Validated {len(json.loads((root / 'catalog.json').read_text()))} portable skills and catalog links.")
