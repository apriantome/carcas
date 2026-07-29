# === Stage 32: Добавь журнал действий пользователя ===
# Project: MeetingNotes
class UserActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user, action_type, description, timestamp=None):
        if timestamp is None:
            import datetime
            timestamp = datetime.datetime.now().isoformat()
        entry = {
            'user': user,
            'type': action_type,
            'description': description,
            'timestamp': timestamp,
        }
        self.entries.append(entry)

    def get_user_history(self, user):
        return [e for e in self.entries if e['user'] == user]

    def summary(self):
        counts = {}
        for e in self.entries:
            key = (e['user'], e['type'])
            counts[key] = counts.get(key, 0) + 1
        return counts
