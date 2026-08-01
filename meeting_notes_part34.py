# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: MeetingNotes
TEMPLATES = {
    "daily": {
        "title_template": "{date:%Y-%m-%d} — Ежедневная встреча",
        "agenda_items": ["Обсудить план на день"],
        "decisions": [],
        "tasks": [],
    },
    "sprint_review": {
        "title_template": "Review спринта {date:%Y-%m-%d}",
        "agenda_items": [
            "Проход по задачам",
            "Обсуждение результатов",
            "Планы на следующий спринт",
        ],
        "decisions": [],
        "tasks": [],
    },
}

def get_template(name):
    if name not in TEMPLATES:
        raise ValueError(f"Unknown template: {name}. Available: {list(TEMPLATES.keys())}")
    return dict(TEMPLATES[name])

def create_meeting_from_template(template_name, **overrides):
    tpl = get_template(template_name)
    meeting = Meeting(
        title=tpl["title_template"].format(**overrides),
        agenda_items=list(tpl["agenda_items"]),
        decisions=[],
        tasks=[],
    )
    return meeting
