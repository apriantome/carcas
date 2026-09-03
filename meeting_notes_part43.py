# === Stage 43: Добавь пагинацию длинных списков ===
# Project: MeetingNotes
def get_paginated(self, items: list, page: int = 1, page_size: int = 10) -> dict:
        """Returns paginated items with metadata."""
        total = len(items)
        start = (page - 1) * page_size
        end = start + page_size
        return {
            "items": items[start:end],
            "page": page,
            "page_size": page_size,
            "total": total,
            "total_pages": (total + page_size - 1) // page_size,
        }
