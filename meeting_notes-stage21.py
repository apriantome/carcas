# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: MeetingNotes
import datetime

def add_reminders():
    reminders = []
    while True:
        date_str = input("Введите дату (YYYY-MM-DD) или 'q' для выхода: ")
        if date_str == "q":
            break
        try:
            due_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            task = input(f"Задача на {date_str}: ")
            reminders.append({"task": task, "due_date": due_date})
        except ValueError:
            print("Неверный формат даты. Попробуйте ещё раз.")

    reminders.sort(key=lambda r: r["due_date"])
    today = datetime.datetime.now().date()
    overdue = [r for r in reminders if r["due_date"] < today]
    upcoming = [r for r in reminders if r["due_date"] >= today]

    print("\n=== Напоминания ===")
    print("СРОЧНЫЕ:")
    for i, r in enumerate(overdue, 1):
        print(f"  {i}. {r['task']} (срок: {r['due_date'].strftime('%d.%m')})")

    if upcoming:
        print("\nБЛИЖАЩИЕСЯ:")
        for i, r in enumerate(upcoming, 1):
            days_left = (r["due_date"] - today).days
            marker = "!" if days_left == 0 else f" ({days_left} дн.)"
            print(f"  {i}. {r['task']}{marker}")

    if not overdue and not upcoming:
        print("Напоминаний нет.")
