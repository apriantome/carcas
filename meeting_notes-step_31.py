# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: MeetingNotes
class ProfileManager:
    def __init__(self):
        self.profiles = {}
        self._active_profile = None

    def add_profile(self, name: str, settings: dict) -> bool:
        if not name or not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Profile name cannot be empty")
        if not isinstance(settings, dict):
            raise TypeError("Settings must be a dictionary")
        self.profiles[name] = settings.copy()
        if self._active_profile is None or self._active_profile != name:
            self.set_active(name)
            return True
        return False

    def set_active(self, profile_name: str) -> bool:
        try:
            self._active_profile = profile_name
            return True
        except Exception:
            raise ValueError(f"Profile '{profile_name}' not found")

    @property
    def active_settings(self):
        if self._active_profile is None and len(self.profiles) > 0:
            first_key = next(iter(self.profiles))
            self.set_active(first_key)
            return self.profiles[first_key]
        return {}

    @classmethod
    def from_dict(cls, data):
        mgr = cls()
        for name, settings in data.items():
            if not isinstance(name, str): continue
            mgr.add_profile(name, settings)
        return mgr
