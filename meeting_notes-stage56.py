# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: MeetingNotes
def update_records_bulk(self, records: list[dict]) -> list[dict]:
    """Массовое обновление выбранных записей.
    
    Ожидаемый формат:
    records = [
        {'id': 1, 'field_name': 'status', 'value': 'completed'},
        {'id': 2, 'field_name': 'end_date', 'value': '2025-06-01'},
    ]
    """
    if not records:
        return []
    
    for rec in records:
        record_id = rec.get('id')
        field_name = rec.get('field_name')
        value = rec.get('value')
        
        if not all([record_id, field_name, value]):
            raise ValueError("Каждая запись должна содержать id, field_name и value")
        
        if record_id not in self._record_map:
            raise KeyError(f"Запись с id={record_id} не найдена")
        
        record = self._record_map[record_id]
        record[field_name] = value
    
    self._save_all()
    return [self._record_map[rec['id']] for rec in records]
