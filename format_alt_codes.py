from pathlib import Path
path = Path('C:/Users/floris/Documents/GitHub/cheatsheet/alt-codes-accent-letters.md')
text = path.read_text(encoding='utf-8')
sections = []
current = None
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('## '):
        if current:
            sections.append(current)
        letter = stripped[3:].strip()
        current = (letter, [])
        continue
    if not current:
        continue
    if not stripped:
        continue
    if stripped.startswith('Alt Codes') and 'Symbol' in stripped:
        continue
    current[1].append(stripped)
if current:
    sections.append(current)
lines_out = ['# Alt Codes Accent Letters', '']
for letter, entries in sections:
    lines_out.append(f'## {letter}')
    lines_out.append('')
    lines_out.append('| Alt Code | Symbol | Description |')
    lines_out.append('| --- | --- | --- |')
    for entry in entries:
        parts = [p.strip() for p in entry.split('\t') if p.strip()]
        if not parts:
            continue
        alt = parts[0]
        symbol = parts[1] if len(parts) > 1 else ''
        desc = ' '.join(parts[2:]) if len(parts) > 2 else ''
        lines_out.append(f'| {alt} | {symbol} | {desc} |')
    lines_out.append('')
path.write_text('\n'.join(lines_out).rstrip() + '\n', encoding='utf-8')
