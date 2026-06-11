# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: MeetingNotes
class MeetingNote:
    def __init__(self, title: str, agenda: list[str], decisions: dict[str, str], tasks: list[dict]):
        self._validate(title, agenda, decisions, tasks)
        self.title = title.strip() or "Без названия"
        self.agenda = [a.strip() for a in agenda if isinstance(a, str)]
        self.decisions = {k.strip(): v.strip() for k, v in decisions.items()}
        self.tasks = tasks

    @staticmethod
    def _validate(title: str, agenda: list, decisions: dict, tasks: list):
        if not title or len(title) > 100: raise ValueError("Некорректный заголовок")
        if not isinstance(agenda, list) or any(not isinstance(a, str) for a in agenda): raise TypeError("Повестка должна быть списком строк")
        if not isinstance(decisions, dict) or any(not isinstance(k, str) and not isinstance(v, str) for k, v in decisions.items()): raise TypeError("Решения должны быть словарём со строковыми ключами и значениями")
        if not isinstance(tasks, list): raise TypeError("Задачи должны быть списком")
