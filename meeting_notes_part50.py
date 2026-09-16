# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: MeetingNotes
def print_report():
    """Показывает краткую сводку по всем встречам."""
    print("=" * 60)
    for i, mtg in enumerate(meetings, 1):
        print(f"Встреча #{i}: {mtg['title']}")
        print(f"  Дата:        {mtg['date']}")
        print(f"  Статус:      {mtg['status']}")
        print(f"  Повестка:    {mtg['agenda']}")
        print(f"  Решения:     {mtg['decisions']}")
        print(f"  Задачи:      {mtg['tasks']}")
        print(f"  Ответственные: {mtg['owners']}")
        print("-" * 60)
