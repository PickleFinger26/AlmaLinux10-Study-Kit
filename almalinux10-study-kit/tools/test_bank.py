import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
lessons = json.loads((ROOT / 'data/lessons.json').read_text())
cards = json.loads((ROOT / 'data/flashcards.json').read_text())
assert len(lessons) == 18
assert len(cards) >= 40
assert len({c['id'] for c in cards}) == len(cards)
assert all(c['lesson'] in {l['id'] for l in lessons} for c in cards)
assert all((ROOT / l['note']).exists() for l in lessons)
assert 'const cards=' in (ROOT/'tools/study.html').read_text()
print(f'OK: {len(lessons)} lessons, {len(cards)} cards, all notes present')
