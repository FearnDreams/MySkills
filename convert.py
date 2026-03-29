#!/usr/bin/env python3
import os, re, json

def parse_skill_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    parts = content.split('\n---\n')
    if len(parts) < 2:
        return None
    frontmatter_text = parts[0].replace('---\n', '')
    main_content = '\n---\n'.join(parts[1:]).lstrip('\n')
    skill_info = {'allowedTools': []}
    in_allowed_tools = False
    for line in frontmatter_text.split('\n'):
        line = line.rstrip()
        if not line: continue
        if line.startswith('allowed-tools:'):
            in_allowed_tools = True
            continue
        elif in_allowed_tools:
            if line.startswith('-') or line.startswith('  -'):
                tool = line.lstrip('- ').strip()
                if tool: skill_info['allowedTools'].append(tool)
            elif line and not line.startswith(' ') and ':' in line:
                in_allowed_tools = False
                k, v = line.split(':', 1)
                skill_info[k.strip()] = v.strip()
            continue
        if ':' in line:
            k, v = line.split(':', 1)
            skill_info[k.strip()] = v.strip()
    return skill_info, main_content

def convert_claude(si, mc, name):
    pm = re.search(r'## Prompt\s*\n+```\s*\n(.*?)```', mc, re.DOTALL)
    p = pm.group(1).strip() if pm else mc.strip()
    p = re.sub(r'```.*?```', '', p, flags=re.DOTALL)
    p = re.sub(r'#{1,6}\s+', '', p)
    p = re.sub(r'\*{1,2}(.*?)\*{1,2}', r'\1', p)
    return {"name": si.get('name', name), "description": si.get('description', ''), "allowedTools": si.get('allowedTools', []), "instruction": p.strip()}

def convert_gpt(si, mc, name):
    pm = re.search(r'## Prompt\s*\n+```\s*\n(.*?)```', mc, re.DOTALL)
    p = pm.group(1).strip() if pm else mc.strip()
    p = re.sub(r'```.*?```', '', p, flags=re.DOTALL)
    p = re.sub(r'#{1,6}\s+', '', p)
    return p.strip()

for cat in ['academic', 'knowledge', 'tools']:
    cp = f'{os.path.dirname(__file__)}/{cat}'
    if not os.path.exists(cp): continue
    for sd in os.listdir(cp):
        sf = os.path.join(cp, sd, 'SKILL.md')
        if not os.path.isfile(sf): continue
        r = parse_skill_md(sf)
        if not r: continue
        si, mc = r
        with open(f'{os.path.dirname(__file__)}/claude/{sd}.json', 'w') as f:
            json.dump(convert_claude(si, mc, sd), f, ensure_ascii=False, indent=2)
        with open(f'{os.path.dirname(__file__)}/gpt/{sd}.md', 'w') as f:
            f.write(convert_gpt(si, mc, sd))
        print(f'Converted: {sd}')
