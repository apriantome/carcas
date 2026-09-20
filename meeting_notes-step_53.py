# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: MeetingNotes
def load_notes_from_text(path):
    """Загружает записи из текстового файла.
    
    Формат файла:
    # Заголовок (опционально)
    Meeting: Планерка
    Date: 2024-01-15
    Agenda: Обсуждение бюджета
    Decisions: Утвердить бюджет на 100к
    Action: Создать отчёт по бюджету
    Owner: Иван Иванов
    
    # Another meeting
    Meeting: Спринт-план
    Date: 2024-01-16
    Agenda: План на следующий спринт
    Decisions: Начать с фич X
    Action: Написать код для X
    Owner: Мария Петрова
    """
    from datetime import datetime
    notes = []
    current = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if ':' not in line:
                continue
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if key == 'Meeting' and value:
                notes.append(current)
                current = {'meeting': value, 'date': '', 'agenda': '', 'decisions': '', 'actions': '', 'owners': ''}
            elif key == 'Meeting' and not value:
                continue
            elif key == 'Date':
                current['date'] = value
            elif key == 'Agenda':
                current['agenda'] = value
            elif key == 'Decisions':
                current['decisions'] = value
            elif key == 'Action':
                current['actions'] = value
            elif key == 'Owner':
                current['owners'] = value
        if current:
            notes.append(current)
    return notes
