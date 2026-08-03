# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: MeetingNotes
def get_next_suggestion(meeting_notes: list, max_suggestions: int = 3) -> list[str]:
    """
    Предлагает следующие шаги на основе истории встреч:
      - если есть незакрытые задачи — напомнить о них;
      - если за последний месяц не было встреч — предложить созвать новую;
      - иначе — подвести итог текущего прогресса.
    """
    suggestions = []

    # Задачи из последней встречи, которые ещё не выполнены
    last_meeting = meeting_notes[-1] if meeting_notes else None
    open_tasks = [
        t for t in (last_meeting.get("tasks") or [])
        if not t.get("done", False) and t.get("assigned_to")
    ]

    # Фиксированные дедлайны — проверяем, не прошли ли они
    overdue = []
    today = datetime.date.today()
    for task in open_tasks:
        deadline_str = task.get("deadline")
        if deadline_str:
            try:
                dl = datetime.datetime.strptime(deadline_str[:10], "%Y-%m-%d").date()
                if dl < today and not task.get("done", False):
                    overdue.append({"task": task, "deadline": deadline_str})
            except ValueError:
                pass

    # Задачи с дедлайном уже прошли — выносим наверх
    if overdue:
        suggestions.append(
            f"⚠️  Упущены дедлайны по задачам:\n" +
            "\n".join(f"   - {t['task'].get('description','?')} (дедлайн: {o['deadline']})" for o in overdue)
        )

    # Оставшиеся незакрытые — мягкое напоминание
    remaining = [t for t in open_tasks if t not in overdue]
    if remaining:
        owners = "; ".join(set(t["assigned_to"] for t in remaining))
        suggestions.append(
            f"📋 Следующие задачи ещё не выполнены:\n   Ответственные: {owners}\n" +
            "\n".join(f"   - {t.get('description','?')}" for t in remaining)
        )

    # Если всё закрыто — предложить новую встречу или подвести итог
    if not open_tasks and meeting_notes:
        last_date = datetime.date.today()
        try:
            last_dt = datetime.datetime.strptime(
                str(meeting_notes[-1].get("date", "")), "%Y-%m-%d"
            ).date()
            gap_days = (last_date - last_dt).days
            if gap_days > 30:
                suggestions.append(
                    f"📅 С последней встречей прошло {gap_days} дней. "
                    "Подведите итоги или созовьте новую."
                )
            else:
                suggestions.append("✅ Все задачи закрыты — отлично! Рассмотрите возможность следующей встречи.")
        except (ValueError, KeyError):
            suggestions.append("✅ Все задачи закрыто — рассмотрите следующий шаг проекта.")

    return suggestions[:max_suggestions]
