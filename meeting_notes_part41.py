# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: MeetingNotes
def dry_run(func, *args, **kwargs):
    """Execute func in a simulated environment by wrapping it with a fake store."""
    original_store = _get_store()
    fake_store = FakeStore()
    _set_store(fake_store)
    try:
        return func(*args, **kwargs)
    finally:
        _set_store(original_store)


class FakeStore:
    def __init__(self):
        self.data = {}
        self.changes = []

    def get(self, key, default=None):
        return self.data.get(key, default)

    def put(self, key, value):
        self.changes.append(("put", key, value))
        self.data[key] = value

    def delete(self, key):
        self.changes.append(("delete", key))
        del self.data[key]

    def get_changes(self):
        return self.changes
