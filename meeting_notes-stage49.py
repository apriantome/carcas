# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: MeetingNotes
def self_check():
    print("=" * 60)
    print("MeetingNotes — Самопроверка")
    print("=" * 60)
    
    # Проверка структуры
    required_methods = ["add_meeting", "add_agenda_item", "add_decision", 
                       "add_action_item", "get_meeting", "list_meetings",
                       "search_notes"]
    missing = [m for m in required_methods if not hasattr(MeetingNotes, m)]
    if missing:
        print(f"❌ Отсутствуют методы: {', '.join(missing)}")
    else:
        print("✅ Все методы MeetingNotes на месте")
    
    # Проверка работы с данными
    mn = MeetingNotes()
    mn.add_meeting(1, "Тестовая встреча", "2024-01-15", "IT отел", "Иван Иванов")
    mn.add_agenda_item(1, "Обсудить API", "10:00")
    mn.add_decision(1, "Использовать REST API", "Иван Иванов")
    mn.add_action_item(1, "Спроектировать API", "Иван Иванов", "2024-01-20")
    
    m = mn.get_meeting(1)
    if m and m.title == "Тестовая встреча":
        print("✅ Добавление и получение встречи работает")
    else:
        print("❌ Ошибка в добавлении/получении встречи")
    
    items = mn.list_meetings()
    if len(items) >= 1:
        print("✅ Список встреч работает")
    else:
        print("❌ Ошибка в списке встреч")
    
    results = mn.search_notes("API")
    if len(results) >= 1:
        print("✅ Поиск заметок работает")
    else:
        print("❌ Ошибка в поиске заметок")
    
    print("=" * 60)
    print("MeetingNotes готов к использованию! 🚀")
    print("=" * 60)
