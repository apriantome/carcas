# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: MeetingNotes
import json
import os

# Функция для миграции структуры данных из старой версии в новую
def migrate_data(data):
    """
    Выполняет миграцию данных из старой версии в новую.
    """
    # Проверяем, если это старая версия данных
    if 'version' not in data or data['version'] < 2:
        # Добавляем новую версию
        data['version'] = 2
        # Проверяем, есть ли список повесток
        if 'agenda' not in data:
            data['agenda'] = []
        # Проверяем, есть ли список решений
        if 'decisions' not in data:
            data['decisions'] = []
        # Проверяем, есть ли список задач
        if 'tasks' not in data:
            data['tasks'] = []
        # Проверяем, есть ли список ответственных
        if 'responsible' not in data:
            data['responsible'] = []
        return data
    return data

# Проверяем, есть ли файл meeting_notes.json
if os.path.exists('meeting_notes.json'):
    # Читаем данные из файла
    with open('meeting_notes.json', 'r') as f:
        data = json.load(f)
    # Выполняем миграцию данных
    data = migrate_data(data)
    # Записываем данные обратно в файл
    with open('meeting_notes.json', 'w') as f:
        json.dump(data, f, indent=2)
else:
    # Если файл не существует, создаём новый
    data = {
        'version': 2,
        'agenda': [],
        'decisions': [],
        'tasks': [],
        'responsible': []
    }
    with open('meeting_notes.json', 'w') as f:
        json.dump(data, f, indent=2)
