# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: MeetingNotes
def delete_meeting(meeting_id: int) -> bool:
    """Удалить встречу по ID, возвращая True если удалено."""
    if meeting_id not in meetings:
        print(f"Встреча с id={meeting_id} не найдена.")
        return False
    
    del meetings[meeting_id]
    print(f"Встреча с id={meeting_id} успешно удалена.")
    return True

def handle_missing_meeting(meeting_id: int) -> None:
    """Обработать случай отсутствия встречи, выводя сообщение."""
    if meeting_id not in meetings:
        print(f"[Предупреждение] Встреча #{meeting_id} не существует в журнале.")
