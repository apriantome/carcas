# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: MeetingNotes
def export_to_text(meetings):
    """Экспортирует список встреч в компактный текстовый отчёт."""
    lines = ["MeetingNotes - Отчёт о встречах\n"]
    lines.append("=" * 40 + "\n")
    for i, m in enumerate(meetings, 1):
        lines.append(f"[{i}] {m['topic']} ({m['date']})\n")
        lines.append(f"    Решение: {m['resolution']}\n")
        for j, t in enumerate(m.get('tasks', []), 1):
            lines.append(f"    - [{j}] {t['task']} -> {t['owner']}")
        lines.append("-" * 40)
    return "\n".join(lines)
