# === Stage 17: Добавь группировку записей по категориям ===
# Project: MeetingNotes
from collections import defaultdict

def group_by_category(records, key_field='category'):
    grouped = defaultdict(list)
    for record in records:
        if isinstance(record.get(key_field), list):
            for cat in record[key_field]:
                grouped[cat].append(record.copy())
        else:
            grouped[str(record.get(key_field)) or 'general'].append(record.copy())
    return dict(grouped)

def get_summary_by_category(records, key_field='category'):
    summary = defaultdict(lambda: {'count': 0, 'tasks': [], 'decisions': []})
    for record in records:
        cat = str(record.get(key_field)) or 'general'
        summary[cat]['count'] += 1
        if record.get('type') == 'task':
            summary[cat]['tasks'].append({
                'description': record['description'],
                'responsible': record.get('responsible'),
                'deadline': record.get('deadline')
            })
        elif record.get('type') == 'decision':
            summary[cat]['decisions'].append(record['description'])
    return dict(summary)
