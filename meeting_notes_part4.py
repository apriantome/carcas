# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: MeetingNotes
def edit_meeting(meeting_id: int, updates: dict) -> MeetingNote | None:
    for i in range(len(meetings)):
        if meetings[i].id == meeting_id:
            updated = MeetingNote(
                id=meetings[i].id,
                agenda=updates.get("agenda", meetings[i].agenda),
                decisions=updates.get("decisions", meetings[i].decisions),
                tasks=updates.get("tasks", meetings[i].tasks),
                owners=updates.get("owners", meetings[i].owners)
            )
            meetings[i] = updated
            return updated
    print(f"Meeting with id {meeting_id} not found.")
    return None
