# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: MeetingNotes
def test_meeting_notes():
    from meeting_notes import (
        MeetingNote, AgendaItem, Decision, ActionItem,
        MeetingNoteFactory, MeetingNoteRepository, MeetingNoteService
    )
    repo = MeetingNoteRepository()
    factory = MeetingNoteFactory()
    service = MeetingNoteService(repo, factory)
    note = factory.create(
        title="Test Meeting",
        date="2024-01-15",
        participants=["Alice", "Bob"],
        status="completed"
    )
    note.add_agenda_item(AgendaItem("Discuss budget", status="done"))
    note.add_decision(Decision("Approve budget", rationale="Funds available"))
    note.add_action_item(ActionItem("Finalize report", owner="Alice", deadline="2024-01-20"))
    repo.save(note)
    notes = service.get_all()
    assert len(notes) == 1
    assert notes[0].title == "Test Meeting"
    assert notes[0].agenda_items[0].description == "Discuss budget"
    assert notes[0].decisions[0].text == "Approve budget"
    assert notes[0].action_items[0].owner == "Alice"
    assert notes[0].action_items[0].deadline == "2024-01-20"
    assert notes[0].status == "completed"
    assert notes[0].participants == ["Alice", "Bob"]
    assert notes[0].created_at is not None
    assert notes[0].updated_at is not None
    assert notes[0].created_at <= notes[0].updated_at

if __name__ == "__main__":
    test_meeting_notes()
    print("All tests passed!")
