# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: MeetingNotes
def check_overdue_reminders(reminders):
    now = datetime.now()
    overdue = []
    for r in reminders:
        if r["date"] < now and (r.get("reminder") is None or not r["reminder"]["sent"]):
            overdue.append(r)
    return overdue

def send_reminder(reminders, user_id=None):
    overdue = check_overdue_reminders(reminders)
    for r in overdue:
        if r.get("user_id") != user_id and r.get("user_id") is not None:
            continue
        name = r["attendee"]["name"]
        date_str = r["date"].strftime("%d.%m.%Y")
        print(f"⏰ Напоминание: {name} — встреча в {date_str}")

if __name__ == "__main__":
    from datetime import datetime
    data = json.load(open("notes.json"))
    attendees = [a for a in data["attendees"] if a.get("role") == "participant" and not a.get("absent", False)]
    reminders = []
    for m in data["meetings"]:
        for i, att in enumerate(m["participants"]):
            name = att["name"]
            date_str = att.get("date", "")
            if name and date_str:
                reminders.append({"attendee": {"name": name}, "date": datetime.strptime(date_str, "%d.%m.%Y")})

    data["reminders"] = reminders
    send_reminder(reminders)
