# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: MeetingNotes
from typing import List, Optional, Callable
import re

def filter_meetings(
    meetings: List[dict],
    status_filter: Optional[str] = None,
    category_filter: Optional[str] = None,
    tag_filters: Optional[List[str]] = None,
) -> List[dict]:
    if not meetings:
        return []

    def matches_status(m: dict) -> bool:
        if not status_filter:
            return True
        m_status = m.get("status", "").lower()
        # Поддержка множественных статусов через запятую или пробелы (например "завершена, в работе")
        filters = [f.strip().lower() for f in re.split(r"[,\s]+", status_filter)]
        return any(f in m_status for f in filters)

    def matches_category(m: dict) -> bool:
        if not category_filter:
            return True
        cat = m.get("category", "").lower()
        # Аналогично для категорий, если введено несколько через запятую/пробел
        filters = [f.strip().lower() for f in re.split(r"[,\s]+", category_filter)]
        return any(f in cat for f in filters)

    def matches_tags(m: dict) -> bool:
        if not tag_filters or "tags" not in m:
            # Если тегов нет в записи, считаем её несовместимой с фильтрацией по тегам (или вернуть True если фильтров нет)
            return len(tag_filters) == 0

        tags = [t.strip().lower() for t in re.split(r"[,\s]+", str(m.get("tags", "")))]
        # Возвращаем True, если хотя бы один из запрошенных тегов найден в записи
        return any(t in tags for t in tag_filters)

    filtered = []
    for m in meetings:
        if matches_status(m) and matches_category(m) and matches_tags(m):
            filtered.append(m)
    return filtered
