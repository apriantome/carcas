# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: MeetingNotes
def print_meeting(meeting):
    """Компактный вывод одной записи встречи."""
    if not meeting:
        return "Нет данных."
    
    title = meeting.get("title", "(без названия)")
    date = meeting.get("date", "")
    location = meeting.get("location", "")
    agenda_items = meeting.get("agenda", [])
    decisions = meeting.get("decisions", [])
    actions = meeting.get("actions", [])

    print(f"{'═'*50}")
    print(f"  📅 {title} [{date}]")
    if location:
        print(f"  📍 {location}")
    print(f"{'─'*50}")

    # Повестка и решения (связанные)
    for item in agenda_items:
        decision = next((d for d in decisions if d.get("related_to") == item), None)
        if decision:
            status = "✅ Принято" if decision.get("status") == "done" else "⏳ В процессе"
            print(f"  • {item} → {decision['description']} [{status}]")
        elif item not in [d.get("related_to", "") for d in decisions]:
            print(f"  • {item}")

    # Задачи и ответственные
    if actions:
        print(f"{'─'*50}")
        print(f"  📋 ЗАДАЧИ:")
        for action in actions:
            assignee = "Никто" if not action.get("assigned_to") else action["assigned_to"]
            deadline = action.get("deadline", "") or "нет дедлайна"
            print(f"     - [{assignee}] {action['description']} (до {deadline})")

    print(f"{'═'*50}")


# Пример: создаём встречу и показываем её
test_meeting = {
    "title": "Спринт-ревью №4",
    "date": "2024-12-15",
    "location": "Конференц-зал A",
    "agenda": ["Обзор задач за спринт", "Оценка бэклога"],
    "decisions": [
        {"description": "Перенести модуль auth на Q1 2025", "related_to": "Обзор задач за спринт", "status": "done"},
        {"description": "Добавить метрики в Jira-дэшборд", "related_to": "Оценка бэклога", "status": "in_progress"},
    ],
    "actions": [
        {"description": "Подготовить демо для стейкхолдеров", "assigned_to": "Анна", "deadline": "2024-12-20"},
        {"description": "Обновить документацию по API", "assigned_to": "Иван", "deadline": "2025-01-10"},
    ],
}

print_meeting(test_meeting)
