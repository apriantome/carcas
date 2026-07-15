# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: MeetingNotes
def print_meeting_report(meetings: list[dict], fmt: str = "compact") -> None:
    """Выводит сводку всех записей встреч в компактном текстовом виде."""
    if not meetings:
        print("Нет сохранённых записей.")
        return

    for i, m in enumerate(meetings, 1):
        name = m.get("name", "Без названия")
        date = m.get("date", "??.??.????")
        agenda = m.get("agenda", "—") or "нет повестки"
        decisions = m.get("decisions", []) or []
        tasks = m.get("tasks", []) or []

        print(f"\n{'─'*50}")
        print(f"[{i}] {name}  ({date})")
        print(f"    Повестка:   {agenda}")
        if decisions:
            print(f"    Решения:")
            for d in decisions:
                print(f"      • {d}")

        tasks_with_owner = [(t, t.get("owner", "—")) for t in tasks]
        if tasks_with_owner:
            header = f"{'#':<3} {'Задание':<40} {'Ответственный'}"
            print(header)
            for idx, (text, owner) in enumerate(tasks_with_owner, 1):
                print(f"{idx:<3} {text:<40} {owner}")

        if not decisions and not tasks_with_owner:
            print("    (без решений и задач)")


if __name__ == "__main__":
    sample = [
        {"name": "Спринт-планирование", "date": "15.03.2026",
         "agenda": "Выбор задач на следующий спринт",
         "decisions": ["Перенести модуль аналитики на 4 марта"],
         "tasks": [
             {"text": "Написать API для отчётов", "owner": "Олег"},
             {"text": "Поднять тестовый сервер",   "owner": "Мария"},
         ]},
        {"name": "Обзор прогресса", "date": "20.03.2026",
         "agenda": "Краткий обзор завершенных задач",
         "decisions": [],
         "tasks": [
             {"text": "Доработать UI дашборда", "owner": ""},
         ]},
    ]
    print_meeting_report(sample)
