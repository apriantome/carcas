# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: MeetingNotes
def reset_demo():
    """Сбрасывает все данные в дефолтные."""
    global meetings, agenda_items, decisions, tasks, attendees, notes
    
    default_meetings = [
        {"id": 100, "title": "Общий план", "date": "2024-09-15",
         "attendees": ["Анна", "Борис"], "notes": "Старт проекта"},
        {"id": 101, "title": "Тех. обсуждение", "date": "2024-09-22",
         "attendees": ["Виктор", "Дарья"], "notes": "Выбор стека"}
    ]
    default_agenda = [
        {"meeting_id": 100, "item": "Определить цели"},
        {"meeting_id": 100, "item": "Назначить ответственного"},
        {"meeting_id": 101, "item": "Обсудить архитектуру"}
    ]
    default_decisions = [
        {"id": 200, "meeting_id": 100, "text": "Начать с MVP"},
        {"id": 201, "meeting_id": 101, "text": "Использовать Python"}
    ]
    default_tasks = [
        {"id": 300, "description": "Написать README", "assignee": "Анна", "status": "done"},
        {"id": 301, "description": "Создать бэкенд", "assignee": "Борис", "status": "in_progress"}
    ]
    
    meetings = default_meetings[:]
    agenda_items = default_agenda[:]
    decisions = default_decisions[:]
    tasks = default_tasks[:]
    attendees = {}

def clear_state():
    """Очищает все данные до пустых списков."""
    global meetings, agenda_items, decisions, tasks, attendees, notes
    
    meetings = []
    agenda_items = []
    decisions = []
    tasks = []
    attendees = {}
    notes = ""

# Инициализация дефолтных данных при старте программы
reset_demo()
