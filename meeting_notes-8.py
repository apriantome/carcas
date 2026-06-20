# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: MeetingNotes
def print_menu():
    print("\n=== Меню MeetingNotes ===")
    print("1. Показать все встречи")
    print("2. Создать новую встречу")
    print("3. Редактировать текущую встречу")
    print("4. Удалить встречу")
    print("5. Вывести повестку дня")
    print("6. Вывести принятые решения")
    print("7. Вывести задачи и ответственных")
    print("0. Выход из программы")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")

def run_cli():
    meetings = []
    current_id = None
    
    def save_meeting(meet):
        nonlocal meetings, current_id
        if meet['id'] is not None and any(m['id'] == meet['id'] for m in meetings):
            idx = next(i for i, m in enumerate(meetings) if m['id'] == meet['id'])
            meetings[idx] = meet
        else:
            current_id = len(meetings) + 1
            meet['id'] = current_id
            meetings.append(meet)

    def load_meeting():
        nonlocal current_id, meetings
        if not meetings:
            print("Нет сохраненных встреч.")
            return None
        idx = get_int_input("\nВведите ID встречи для редактирования (или 0 чтобы отменить): ")
        if idx == 0:
            return None
        try:
            current_id = int(idx)
            for i, m in enumerate(meetings):
                if m['id'] == current_id:
                    return meetings[i]
        except ValueError:
            pass
        print("Встреча с таким ID не найдена.")
        return None

    def delete_meeting():
        nonlocal current_id, meetings
        if not meetings or current_id is None:
            print("Нет выбранной встречи для удаления.")
            return False
        confirm = input(f"Удалить встречу #{current_id}? (y/n): ").lower()
        if confirm == 'y':
            for i, m in enumerate(meetings):
                if m['id'] == current_id:
                    meetings.pop(i)
                    print("Встреча удалена.")
                    return True
        else:
            print("Удаление отменено.")
        return False

    def show_meeting():
        nonlocal current_id, meetings
        if not meetings or current_id is None:
            print("Нет выбранной встречи для просмотра.")
            return
        for m in meetings:
            if m['id'] == current_id:
                print(f"\n=== Встреча #{m['id']} ===")
                print(f"Дата: {m.get('date', 'Не указано')}")
                print(f"Тема: {m.get('topic', 'Нет темы')}")
                if m.get('agenda'):
                    for item in m['agenda']:
                        print(f"- [{item.get('status', '')}] {item.get('text', '')}")
