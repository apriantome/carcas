# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: MeetingNotes
def validate_and_repair(entries):
    """Проверяет целостность записей и пытается исправить типичные ошибки."""
    repaired = []
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            print(f"Ошибка: запись {i} не является словарём")
            continue
        required = {"title", "agenda", "decisions", "action_items"}
        missing = required - entry.keys()
        if missing:
            print(f"Ошибка: запись {i} пропускает поля: {missing}")
            continue
        try:
            entry.setdefault("agenda", [])
            entry.setdefault("decisions", [])
            entry.setdefault("action_items", [])
            for item in entry["action_items"]:
                if not isinstance(item, dict) or "assignee" not in item or "task" not in item:
                    print(f"Ошибка: задача в {i} некорректна")
                    break
            repaired.append(entry)
        except Exception as e:
            print(f"Ошибка: запись {i} повреждена: {e}")
    return repaired
