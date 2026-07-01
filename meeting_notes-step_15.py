# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: MeetingNotes
def generate_weekly_stats(meetings):
    from collections import defaultdict
    if not meetings: return {}
    stats = defaultdict(lambda: {'count': 0, 'total_duration_min': 0})
    for m in meetings:
        date_str = m.get('date') or ''
        if not date_str: continue
        try:
            dt = datetime.strptime(date_str, '%Y-%m-%d').date()
            week_start = (dt - timedelta(days=dt.weekday())).isoformat()
            key = f"{week_start}+7"
            stats[key]['count'] += 1
            if 'duration_min' in m:
                stats[key]['total_duration_min'] += int(m['duration_min'])
        except ValueError: continue
    return {k.replace('+7', ''): {'count': v['count'], 'avg_duration_min': round(v['total_duration_min']/v['count'], 1) if v['count'] else 0} for k, v in stats.items()}
