# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: MeetingNotes
def sort_meetings(meeting_list, key='date'):
    if not meeting_list: return []
    reverse = {'date': True, 'priority': False, 'name': False}.get(key, True)
    def get_sort_key(m):
        val = m.get(key, '')
        if key == 'priority': return 4 - int(val) or 0
        if isinstance(val, str): return (0, val.lower())
        return (1, val)
    return sorted(meeting_list, key=get_sort_key, reverse=reverse)
