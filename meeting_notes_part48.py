# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: MeetingNotes
def _split_agenda_item(line: str) -> dict[str, str]:
    """Parse an agenda line into topic, subtopic, description."""
    topic, subtopic, desc = "", "", ""
    if subtopic := line.split("::", 1)[1]:
        topic = line.split("::", 1)[0]
        desc = subtopic.split("::", 1)[1] if "::" in subtopic else subtopic
    else:
        desc = line
    return {"topic": topic, "subtopic": subtopic, "description": desc}

def _parse_decision(line: str) -> dict[str, str]:
    """Parse a decision line into decision, reason, action."""
    parts = line.split("::", 2)
    return {
        "decision": parts[0],
        "reason": parts[1] if len(parts) > 1 else "",
        "action": parts[2] if len(parts) > 2 else "",
    }

def _parse_task(line: str) -> dict[str, str]:
    """Parse a task line into task, owner, deadline."""
    task, owner, deadline = "", "", ""
    if owner := line.split("::", 1)[1]:
        task = line.split("::", 1)[0]
        if deadline := owner.split("::", 1)[1]:
            owner = owner.split("::", 1)[0]
    return {"task": task, "owner": owner, "deadline": deadline}

def _format_agenda_item(item: dict[str, str]) -> str:
    return f"{item['topic']}::{item['subtopic']}::{item['description']}"

def _format_decision(decision: dict[str, str]) -> str:
    return f"{decision['decision']}::{decision['reason']}::{decision['action']}"

def _format_task(task: dict[str, str]) -> str:
    return f"{task['task']}::{task['owner']}::{task['deadline']}"
