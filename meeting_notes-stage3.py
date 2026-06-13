# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: MeetingNotes
class MeetingNotes:
    def __init__(self):
        self._records = []
    
    def add_meeting(self, agenda_items, decisions, tasks_with_responsible):
        record = {
            'agenda': agenda_items,
            'decisions': decisions,
            'tasks': tasks_with_responsible,
            'timestamp': datetime.now().isoformat()
        }
        self._records.append(record)
        return len(self._records)
