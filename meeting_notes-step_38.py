# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: MeetingNotes
import pytest

class TestEdgeCasesAndErrors:
    def test_empty_agenda(self):
        meeting = Meeting()
        meeting.add_agenda_item("", "")
        assert meeting.items[-1].topic == ""
        assert meeting.items[-1].description == ""

    def test_add_item_during_processing(self):
        meeting = Meeting()
        meeting.add_agenda_item("Пункт А", "Описание А")
        meeting.process_agenda_item(0, "Решено", "Иван")
        with pytest.raises(ValueError, match="cannot add"):
            meeting.add_agenda_item("Пункт Б", "Описание Б")

    def test_remove_item_during_processing(self):
        meeting = Meeting()
        meeting.add_agenda_item("Пункт А", "Описание А")
        meeting.process_agenda_item(0, "Решено", "Иван")
        with pytest.raises(ValueError, match="cannot remove"):
            meeting.remove_agenda_item(0)

    def test_remove_last_item(self):
        meeting = Meeting()
        meeting.add_agenda_item("Пункт А", "Описание А")
        meeting.process_agenda_item(0, "Решено", "Иван")
        meeting.remove_agenda_item(0)
        assert len(meeting.items) == 0

    def test_remove_nonexistent_item(self):
        meeting = Meeting()
        meeting.add_agenda_item("Пункт А", "Описание А")
        with pytest.raises(ValueError, match="No item at index"):
            meeting.remove_agenda_item(99)

    def test_assign_task_to_nonexistent_person(self):
        meeting = Meeting()
        meeting.add_agenda_item("Пункт А", "Описание А")
        meeting.process_agenda_item(0, "Решено", "Иван")
        meeting.assign_task(0, "Павел", "Задача 1")
        with pytest.raises(ValueError, match="no such person"):
            meeting.assign_task(0, "Павел", "Задача 1")

    def test_remove_task_from_nonexistent_person(self):
        meeting = Meeting()
        meeting.add_agenda_item("Пункт А", "Описание А")
        meeting.process_agenda_item(0, "Решено", "Иван")
        meeting.assign_task(0, "Иван", "Задача 1")
        with pytest.raises(ValueError, match="no such person"):
            meeting.remove_task(0, "Павел")

    def test_duplicate_decision(self):
        meeting = Meeting()
        meeting.add_agenda_item("Пункт А", "Описание А")
        meeting.process_agenda_item(0, "Решено", "Иван")
        with pytest.raises(ValueError, match="already decided"):
            meeting.make_decision(0, "Решено", "Иван")

    def test_empty_title(self):
        meeting = Meeting()
        meeting.set_title("")
        assert meeting.title == ""

    def test_empty_date(self):
        meeting = Meeting()
        meeting.set_date("")
        assert meeting.date == ""

    def test_empty_participants(self):
        meeting = Meeting()
        meeting.set_participants([])
        assert meeting.participants == []

    def test_add_task_after_done(self):
        meeting = Meeting()
        meeting.add_agenda_item("Пункт А", "Описание А")
        meeting.process_agenda_item(0, "Решено", "Иван")
        meeting.assign_task(0, "Иван", "Задача 1")
        meeting.remove_task(0, "Иван")
        with pytest.raises(ValueError, match="already done"):
            meeting.assign_task(0, "Иван", "Задача 2")

    def test_remove_task_after_done(self):
        meeting = Meeting()
        meeting.add_agenda_item("Пункт А", "Описание А")
        meeting.process_agenda_item(0, "Решено", "Иван")
        meeting.assign_task(0, "Иван", "Задача 1")
        meeting.remove_task(0, "Иван")
        with pytest.raises(ValueError, match="already done"):
            meeting.remove_task(0, "Иван")
