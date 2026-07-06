# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: MeetingNotes
class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Tag '{self.name}'>"

    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.name == other.name
        return NotImplemented


class Meeting:
    def __init__(self, title, date=None, tags=None):
        self.title = title
        self.date = date
        self.tags = set(tags) if tags else set()

    def add_tag(self, name):
        tag = Tag(name.lower())
        self.tags.add(tag)
        return tag

    def remove_tag(self, name):
        tag = Tag(name.lower())
        if tag in self.tags:
            self.tags.discard(tag)
            return True
        return False


class Journal:
    def __init__(self):
        self.meetings = []

    def add_meeting(self, title, date=None, tags=None):
        meeting = Meeting(title, date, tags)
        self.meetings.append(meeting)
        return meeting
