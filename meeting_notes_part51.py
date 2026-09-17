# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: MeetingNotes
class ChangeLog:
    def __init__(self):
        self._entries = []

    def log(self, category, description, actor=None, timestamp=None):
        from datetime import datetime
        ts = timestamp or datetime.now()
        self._entries.append({
            'timestamp': ts,
            'category': category,
            'description': description,
            'actor': actor,
        })

    def get_changes(self, category=None):
        if category:
            return self._entries[-10:]
        return self._entries[-10:]
