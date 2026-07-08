# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: MeetingNotes
def archive_old_records(records, cutoff_days=365):
    """Archive records older than cutoff_days."""
    import datetime
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(days=cutoff_days)
    archived = []
    active = []
    for r in records:
        if r['date'] < cutoff:
            r['status'] = 'archived'
            archived.append(r)
        else:
            active.append(r)
    return active, archived
