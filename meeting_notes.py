# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: MeetingNotes
# MeetingNotes Application

def main():
    # Инициализация данных (в реальном проекте здесь был бы загрузчик из БД или файла)
    meetings = [
        {
            "id": 1,
            "title": "Обсуждение архитектуры",
            "date": "2023-10-27",
            "agenda": ["Выбор фреймворка", "Планирование базы данных"],
            "decisions": ["Выбран Django", "Используем PostgreSQL"],
            "tasks": [
                {"text": "Настроить окружение", "owner": "Олег", "status": "done"},
                {"text": "Спроектировать схему БД", "owner": "Анна", "status": "pending"}
            ]
        }
    ]

    # Точка входа: вывод демо-данных для проверки структуры
    print(f"Загружено встреч: {len(meetings)}")
    for meeting in meetings:
        print(f"\nВстреча от {meeting['date']}: {meeting['title']}")
        print(f"  Решения: {', '.join(meeting['decisions'])}")
        for task in meeting['tasks']:
            status_mark = "✓" if task['status'] == 'done' else "○"
            print(f"  [{task['owner']}] {task['text']} [{status_mark}]")

if __name__ == "__main__":
    main()
