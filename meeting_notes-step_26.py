# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: MeetingNotes
import json, sys
from meeting_notes import MeetingNote


def demo():
    note = MeetingNote()
    note.add_agenda("Обзор проекта")
    note.add_decision("Выбрать Python", "Python 3.12+")
    note.add_action("Написать README", "Иван Иванов", 0)

    print("=" * 40)
    print(f"Тема: {note.agenda}")
    print("-" * 40)
    for i, (action, who, deadline) in enumerate(note.actions.items(), 1):
        print(f"{i}. [{deadline}] {action} — ответственный: {who}")
    print("=" * 40)


demo()
