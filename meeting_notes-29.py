# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: MeetingNotes
DEFAULT_CONFIG = {
    "max_notes": 100,
    "date_format": "%Y-%m-%d",
    "time_format": "%H:%M",
    "default_priority": "medium",
    "allowed_priorities": ["low", "medium", "high"],
}


def load_config():
    config = DEFAULT_CONFIG.copy()
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            user_settings = json.load(f)
            for key in DEFAULT_CONFIG:
                if key in user_settings and isinstance(user_settings[key], (str, int, float, bool)):
                    config[key] = user_settings[key]
    return config


def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=2)
