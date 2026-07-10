# === Stage 20: Добавь восстановление записей из архива ===
# Project: MeetingNotes
def load_from_archive(archive_path):
    """Восстанавливает записи из архива .json, который может содержать как старые, так и новые данные."""
    import json, os
    if not os.path.exists(archive_path):
        print(f"[MeetingNotes] Архив не найден: {archive_path}")
        return []
    with open(archive_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    records = data if isinstance(data, list) else [data]
    for r in records:
        if not isinstance(r, dict):
            print("[MeetingNotes] Пропущена невалидная запись из архива.")
            continue
        r.setdefault('status', 'archived')
        r.setdefault('recovered_at', None)
        import datetime
        r['recovered_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    return records

def export_to_archive(records, archive_path):
    """Экспортирует текущие записи в архив для последующего восстановления."""
    import json
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
