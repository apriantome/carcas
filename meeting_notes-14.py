# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: MeetingNotes
def generate_summary(meetings):
    if not meetings:
        return "Нет данных для сводки."
    
    total_meetings = len(meetings)
    topics_count = len(set(item.get('topic', '') for item in meetings))
    decisions_count = sum(1 for m in meetings for d in m.get('decisions', []))
    tasks_count = sum(len(m.get('tasks', [])) for m in meetings)
    
    overdue_tasks = 0
    now = datetime.now()
    for meeting in meetings:
        for task in meeting.get('tasks', []):
            if task.get('status') == 'pending' and task.get('due_date'):
                due = datetime.strptime(task['due_date'], '%Y-%m-%d').date()
                if now.date() > due:
                    overdue_tasks += 1
    
    summary_lines = [
        f"Сводка по {total_meetings} встречам:",
        f"- Уникальные темы повестки: {topics_count}",
        f"- Принятых решений всего: {decisions_count}",
        f"- Создано задач: {tasks_count}",
        f"- Просрочено задач: {overdue_tasks}"
    ]
    
    return "\n".join(summary_lines)
