# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: MeetingNotes
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки в структуру проекта."""
    try:
        data = json.loads(json_string)
        
        # Валидация обязательных полей
        required_fields = ['meetings', 'users']
        for field in required_fields:
            if not isinstance(data.get(field), list):
                raise ValueError(f"Отсутствует или неверно типизировано поле '{field}'")
            
            # Проверка уникальности ID внутри списков
            ids = [item.get('id') or item['id'] for item in data[field]]
            if len(ids) != len(set(ids)):
                raise ValueError(f"Нарушена уникальность id в списке '{field}'")

        return {
            'meetings': data.get('meetings', []),
            'users': data.get('users', []),
            'config': data.get('config', {})
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)

def init_database(json_string: str, db_path: Path = None):
    """Инициализирует базу данных из строки и сохраняет её."""
    if not json_string.strip():
        print("Предупреждение: JSON-строка пуста. База не инициализирована.")
        return {}

    initial_data = load_initial_data(json_string)
    
    # Сохранение в файл, если указан путь
    if db_path and db_path.exists():
        with open(db_path, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=2)
        print(f"Данные сохранены в {db_path}")
    
    return initial_data

# Пример использования (раскомментируйте для запуска):
if __name__ == "__main__":
    # JSON-строка с начальными данными
    json_string = '''
    {
        "meetings": [
            {"id": 1, "title": "Стартовый митинг", "date": "2023-10-01"},
            {"id": 2, "title": "Обсуждение API", "date": "2023-10-05"}
        ],
        "users": [
            {"id": 1, "name": "Иван Иванов", "email": "ivan@example.com"},
            {"id": 2, "name": "Петр Петров", "email": "petr@example.com"}
        ]
    }
    '''
    
    # Инициализация (можно передать путь к файлу базы данных)
    db = init_database(json_string)
    print(f"Загружено встреч: {len(db['meetings'])}, пользователей: {len(db['users'])}")
