# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: MeetingNotes
def get_selected_notes():
    selected = []
    for i, note in enumerate(notes):
        if note.get("selected", False):
            selected.append((i, note))
    return selected

def toggle_note_selection(index):
    if index < len(notes):
        notes[index]["selected"] = not notes[index].get("selected", False)

def clear_all_selection():
    for note in notes:
        note["selected"] = False
