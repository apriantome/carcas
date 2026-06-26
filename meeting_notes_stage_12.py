# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: MeetingNotes
import json, os, sys

def load_meetings_from_file(file_path: str) -> list[dict]:
    if not file_path or not isinstance(file_path, str):
        print("Ошибка: путь к файлу не указан или неверен.")
        return []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                for item in data:
                    if not isinstance(item, dict):
                        print(f"Предупреждение: пропущен невалидный элемент в файле {file_path}")
                        continue
                return data
            else:
                print("Ошибка: JSON файл должен содержать массив объектов.")
                return []
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден. Загрузка из памяти продолжится.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле '{file_path}': {e}")
        return []
    except PermissionError:
        print(f"Нет доступа к чтению файла '{file_path}'.")
        return []

# Пример вызова (раскомментируйте для теста):
# meetings = load_meetings_from_file("data/meetings.json")
