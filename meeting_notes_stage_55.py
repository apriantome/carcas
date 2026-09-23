# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: MeetingNotes
def _check_duplicate_agenda(meeting_id, agenda_item):
    if meeting_id is None:
        return False
    for item in meeting.agenda:
        if item.title == agenda_item.title and item.description == agenda_item.description:
            return True
    return False

def _check_duplicate_decision(meeting_id, decision):
    if meeting_id is None:
        return False
    for item in meeting.decisions:
        if item.title == decision.title and item.description == decision.description:
            return True
    return False

def _check_duplicate_action(meeting_id, action):
    if meeting_id is None:
        return False
    for item in meeting.actions:
        if (item.title == action.title and item.description == action.description
                and item.owner == action.owner):
            return True
    return False
