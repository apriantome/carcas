# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: MeetingNotes
def sanitize_date(raw):
    """Парсит дату в формате ДД.ММ.ГГГГ, возвращая datetime или сообщение об ошибке."""
    try:
        import datetime
        parts = raw.strip().split('.')
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            return f"Ошибка: '{raw}' — некорректный формат даты. Ожидайте ДД.ММ.ГГГГ."

        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
            return f"Ошибка: '{raw}' — значения выходят за допустимые пределы."

        return datetime.date(year, month, day)
    except Exception as e:
        return f"Ошибка при парсинге даты: {e}"
