# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: MeetingNotes
def export_to_json():
    import json
    data = {
        "meetings": [m.to_dict() for m in meetings],
        "settings": settings,
        "version": 10
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
