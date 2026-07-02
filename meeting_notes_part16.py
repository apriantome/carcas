# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: MeetingNotes
def generate_monthly_stats(meetings):
    from datetime import date, timedelta
    today = date.today()
    current_month_start = date(today.year, today.month, 1)
    stats = {}
    for meeting in meetings:
        try:
            d = date.fromisoformat(meeting['date'])
            if d >= current_month_start and d < (current_month_start + timedelta(days=32)):
                month_key = f"{d.year}-{d.month}"
                if month_key not in stats:
                    stats[month_key] = {'total': 0, 'decisions': [], 'tasks': []}
                stats[month_key]['total'] += 1
                for decision in meeting.get('decisions', []):
                    stats[month_key]['decisions'].append(decision)
                for task in meeting.get('tasks', []):
                    if not task.get('completed'):
                        stats[month_key]['tasks'].append(task['description'])
        except (ValueError, TypeError):
            continue
    return stats
