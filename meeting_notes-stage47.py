# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: MeetingNotes
def demo():
    journal = MeetingJournal()

    journal.add_meeting(
        title="Презентация нового API",
        date=datetime(2024, 11, 15),
        agenda=["Обзор API", "Обсуждение rate-limit", "Вопросы по документации"],
        decisions=[
            "Принять rate-limit 100 req/min для free-плана",
            "Запустить API 1.0 15 ноября"
        ],
        tasks=[
            {"task": "Написать документацию по endpoints", "assignee": "Анна", "deadline": datetime(2024, 11, 22)},
            {"task": "Протестировать rate-limit", "assignee": "Михаил", "deadline": datetime(2024, 11, 20)},
            {"task": "Подготовить пример кода для README", "assignee": "Дмитрий", "deadline": datetime(2024, 11, 25)},
        ],
        notes="Фокус на простоте интеграции для стартапов."
    )

    journal.add_meeting(
        title="Ретроспектива за неделю",
        date=datetime(2024, 11, 22),
        agenda=["Что прошло хорошо", "Что улучшить"],
        decisions=["Перенести демо на пятницу"],
        tasks=[
            {"task": "Добавить dark mode", "assignee": "Анна", "deadline": datetime(2024, 11, 29)}
        ],
        notes="Команда в хорошем темпе."
    )

    print(journal)
