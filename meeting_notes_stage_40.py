# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: MeetingNotes
import argparse

def main():
    parser = argparse.ArgumentParser(description="MeetingNotes CLI")
    parser.add_argument("command", choices=["add", "list", "show"], help="Команда")
    parser.add_argument("--id", type=int, help="ID встречи")
    parser.add_argument("--title", help="Тема встречи")
    parser.add_argument("--agenda", help="Повестка")
    parser.add_argument("--decisions", help="Решения")
    parser.add_argument("--tasks", help="Задачи")
    parser.add_argument("--assignees", help="Ответственные")
    args = parser.parse_args()
    if args.command == "add":
        if not all([args.title, args.agenda, args.decisions, args.tasks, args.assignees]):
            print("Ошибка: нужны все параметры для добавления")
            return
        add_meeting(args)
    elif args.command == "list":
        list_meetings(args)
    elif args.command == "show":
        show_meeting(args)
