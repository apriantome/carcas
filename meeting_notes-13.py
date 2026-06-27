# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: MeetingNotes
def search_meetings(query: str) -> list[dict]:
    query = query.lower().strip()
    if not query:
        return []
    
    results = []
    for meeting in meetings_db:
        text_parts = [
            (meeting.get('title') or '').lower(),
            (meeting.get('topic') or '').lower(),
            ' '.join(meeting.get('decisions', [])).lower(),
            ' '.join(f"{task['description']} {task.get('assignee', '')}" for task in meeting.get('tasks', [])),
        ]
        
        if any(query in part for part in text_parts):
            results.append(meeting)
    
    return results
