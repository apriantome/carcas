# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: MeetingNotes
import json, os
from datetime import datetime

def save_to_file(meeting_notes):
    filename = "meeting_notes.json"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(meeting_notes, f, ensure_ascii=False, indent=2)
        print(f"[OK] Данные сохранены в {filename}")
    except Exception as e:
        print(f"[ERROR] Не удалось сохранить файл: {e}")

def load_from_file():
    filename = "meeting_notes.json"
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"[OK] Загружено {len(data)} записей из {filename}")
        return data
    except Exception as e:
        print(f"[ERROR] Ошибка чтения файла: {e}")
        return []

# Инициализация данных при старте приложения
notes = load_from_file()
