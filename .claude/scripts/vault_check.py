#!/usr/bin/env python3
"""Health check for the Quotr Obsidian vault.

Run from anywhere:  python3 .claude/scripts/vault_check.py
Checks: note names are unique; properties are valid YAML, use the types in
.obsidian/types.json and include the required fields; every [[link]] and
![[embed]] points to a real note, heading or Bases view; .base files are valid.
Exits with code 1 if it finds problems.
"""
import os, re, sys, json, datetime
try:
    import yaml
except ImportError:
    sys.exit('PyYAML is missing: run "pip install pyyaml" and try again.')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SKIP_DIRS = {'.git', '.obsidian', '.trash', '.claude', 'node_modules'}
TEMPLATES = 'geo-brain/_meta/note-templates/'
REQUIRED = {
    'prompt': ['id', 'prompt', 'stage', 'group', 'persona', 'trade', 'intent', 'priority', 'page_status'],
    'test-run': ['date', 'engine', 'test_id', 'test_set', 'prompt_note', 'prompt'],
    'roadmap-item': ['id', 'title', 'cluster', 'priority', 'status'],
    'task': ['id', 'task', 'phase', 'rank', 'status'],
    'question': ['id', 'question', 'topic', 'ask', 'status'],
    'article': ['id', 'title', 'quotr_url', 'published', 'cluster', 'health', 'action', 'priority', 'status'],
}
PAGE_TYPES = {'overview', 'fact-sheet', 'guide', 'baseline', 'competitor', 'hub', 'plan', 'playbook',
              'page-template', 'reference', 'log'}
STATUS = {
    'task': {'todo', 'doing', 'blocked', 'done', 'dropped'},
    'roadmap-item': {'planned', 'writing', 'published', 'refreshed', 'dropped'},
    'question': {'open', 'answered'},
    'article': {'ok', 'todo', 'doing', 'done', 'dropped'},
}
problems = []

def problem(path, msg):
    problems.append(f'{path}: {msg}')

def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, '/')

def walk():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            yield rel(os.path.join(dirpath, f))

def norm_heading(h):
    """Obsidian compares headings with punctuation replaced by spaces, case-insensitively."""
    h = re.sub(r'[!"#$%&()*+,.:;<=>?@^`{|}~/\[\]\\\r\n]', ' ', h)
    return re.sub(r'\s+', ' ', h).strip().lower()

def split_frontmatter(text):
    if not text.startswith('---\n'):
        return None, text
    end = text.find('\n---\n', 4)
    if end == -1:
        end = text.find('\n---', 4)
        if end == -1 or text[end + 4:].strip():
            return 'BROKEN', text
    return text[4:end], text[end + 5:]

def strip_code(body):
    body = re.sub(r'^```.*?^```', lambda m: '\n' * m.group(0).count('\n'), body, flags=re.S | re.M)
    return re.sub(r'`[^`\n]*`', '', body)

def main():
    files = sorted(walk())
    md = [f for f in files if f.endswith('.md')]
    by_name, by_path = {}, {}
    for f in files:
        base = os.path.basename(f)
        key = base[:-3] if f.endswith('.md') else base
        by_name.setdefault(key.lower(), []).append(f)
        by_path[(f[:-3] if f.endswith('.md') else f).lower()] = f
    for name, paths in by_name.items():
        mds = [p for p in paths if p.endswith('.md')]
        if len(mds) > 1:
            problem(', '.join(mds), f'two notes share the name "{name}"; links cannot tell them apart')

    types_path = os.path.join(ROOT, '.obsidian', 'types.json')
    types = json.load(open(types_path))['types'] if os.path.exists(types_path) else {}

    texts, headings, fms = {}, {}, {}
    for f in md:
        text = open(os.path.join(ROOT, f), encoding='utf-8').read()
        fm_text, body = split_frontmatter(text)
        fm = {}
        if fm_text == 'BROKEN':
            problem(f, 'properties block is not closed with ---')
        elif fm_text is not None:
            try:
                fm = yaml.safe_load(fm_text) or {}
                if not isinstance(fm, dict):
                    problem(f, 'properties are not a list of name: value pairs'); fm = {}
            except yaml.YAMLError as e:
                problem(f, f'properties are not valid YAML ({str(e).splitlines()[0]})')
        texts[f], fms[f] = body, fm
        headings[f] = {norm_heading(m.group(1)) for m in re.finditer(r'^#{1,6}\s+(.+?)\s*#*$', strip_code(body), re.M)}

    base_views = {}
    for f in [x for x in files if x.endswith('.base')]:
        try:
            data = yaml.safe_load(open(os.path.join(ROOT, f), encoding='utf-8')) or {}
        except yaml.YAMLError as e:
            problem(f, f'not valid YAML ({str(e).splitlines()[0]})'); continue
        views = data.get('views') or []
        names = [v.get('name') for v in views if isinstance(v, dict)]
        if len(names) != len(set(names)):
            problem(f, 'two views have the same name')
        base_views[f] = set(names)
        for key in ('newItemFolder', 'newItemTemplate'):
            target = data.get(key)
            if target and not os.path.exists(os.path.join(ROOT, target)):
                problem(f, f'{key} points to "{target}", which does not exist')
        for v in views:
            for k in ('order', 'sort'):
                for item in v.get(k) or []:
                    prop = item['property'] if isinstance(item, dict) else item
                    if isinstance(prop, str) and prop.startswith('formula.') and prop[8:] not in (data.get('formulas') or {}):
                        problem(f, f'view "{v.get("name")}" uses {prop}, which is not defined in formulas')

    def resolve(target, src):
        """Return the file a link target points to, or None."""
        t = target.strip()
        if not t:
            return src
        low = t.lower()
        if low in by_path:
            return by_path[low]
        cands = by_name.get(os.path.basename(low)) or by_name.get(os.path.basename(low)[:-3] if low.endswith('.md') else '')
        return cands[0] if cands else None

    link_re = re.compile(r'(!?)\[\[([^\]\n]+?)\]\]')
    for f in md:
        fm = fms[f]
        sources = [strip_code(texts[f])] + [json.dumps(fm, default=str)]
        for chunk in sources:
            for m in link_re.finditer(chunk):
                inner = m.group(2).replace('\\|', '|')
                target, _, _alias = inner.partition('|')
                path, _, sub = target.partition('#')
                dest = resolve(path, f)
                if dest is None:
                    problem(f, f'link to missing note [[{target}]]'); continue
                if sub and dest.endswith('.md') and not sub.startswith('^'):
                    for part in sub.split('#'):
                        if norm_heading(part) not in headings.get(dest, set()):
                            problem(f, f'link to missing heading [[{target}]]'); break
                if sub and dest.endswith('.base') and sub not in base_views.get(dest, set()):
                    problem(f, f'embed of missing view [[{target}]]')
        for m in re.finditer(r'(?<!!)\[[^\]\n]*\]\((?!https?:|mailto:|#)([^)\s]+\.md[^)]*)\)', strip_code(texts[f])):
            problem(f, f'Markdown link to a note ({m.group(1)}): use a [[wikilink]] instead')

        if f.startswith(TEMPLATES) or f.startswith('journal/'):
            continue
        typ = fm.get('type')
        if f.startswith('geo-brain/') and not f.startswith('geo-brain/_exports/') and not typ:
            problem(f, 'no type property')
        for key in REQUIRED.get(typ, []):
            if fm.get(key) in (None, '', []):
                problem(f, f'missing property "{key}" (required for type {typ})')
        if typ in PAGE_TYPES and not fm.get('description'):
            problem(f, 'missing property "description"')
        if typ in STATUS and fm.get('status') not in STATUS[typ]:
            problem(f, f'status "{fm.get("status")}" is not one of: {", ".join(sorted(STATUS[typ]))}')
        for key, val in fm.items():
            want = types.get(key)
            if val is None or want is None:
                continue
            ok = {
                'multitext': isinstance(val, list), 'aliases': isinstance(val, list), 'tags': isinstance(val, list),
                'number': isinstance(val, (int, float)) and not isinstance(val, bool),
                'checkbox': isinstance(val, bool),
                'date': isinstance(val, datetime.date) or (isinstance(val, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}', val)),
                'datetime': isinstance(val, (datetime.date, str)),
                'text': isinstance(val, (str, int, float)) and not isinstance(val, bool),
            }.get(want, True)
            if not ok:
                problem(f, f'property "{key}" should be {want} but is {type(val).__name__}')
    for p in problems:
        print('-', p)
    print(f'Checked {len(md)} notes and {len(base_views)} bases: {len(problems)} problem{"s" if len(problems) != 1 else ""}')
    return 1 if problems else 0

if __name__ == '__main__':
    sys.exit(main())
