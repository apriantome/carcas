# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: MeetingNotes
def print_project_metrics():
    total_meetings = len(meeting_notes)
    total_agendas = sum(len(m['agenda']) for m in meeting_notes if 'agenda' in m)
    total_decisions = sum(len(m['decisions'] or []) for m in meeting_notes)
    total_actions = sum(len(m['actions'] or []) for m in meeting_notes)
    responsible_count = 0
    for m in meeting_notes:
        if 'assignees' in m and m['assignees']:
            responsible_count += len(m['assignees'])

    print(f"Total meetings: {total_meetings}")
    print(f"Total agenda items: {total_agendas}")
    print(f"Total decisions made: {total_decisions}")
    print(f"Total action items: {total_actions}")
    print(f"People assigned to tasks: {responsible_count}")

if __name__ == "__main__":
    print_project_metrics()
