# === Stage 45: Добавь восстановление из резервной копии ===
# Project: MeetingNotes
def load_from_backup(file_path):
    """Восстановить данные из резервной копии."""
    backup_file = file_path + ".backup"
    if not os.path.exists(backup_file):
        print("Резервная копия не найдена.")
        return False
    try:
        with open(backup_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        print("Резервная копия успешно загружена.")
        return True
    except Exception as e:
        print(f"Ошибка при загрузке резервной копии: {e}")
        return False
