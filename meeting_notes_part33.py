# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: MeetingNotes
def roll_back_last():
    """Откат последнего действия в истории: удаляет последний записанный элемент и возвращает его."""
    if not history:
        print("История пуста, откатить нечего.")
        return None
    item = history.pop()
    print(f"Отменено действие: {item}")
    return item

def add_agenda_item(name):
    """Добавляет повестку дня в историю и отображает её."""
    history.append({"type": "agenda", "data": name})
    print(f"Повестка добавлена: {name}")

add_agenda_item("Обсудить бюджет")
roll_back_last()  # <-- откат последнего действия
