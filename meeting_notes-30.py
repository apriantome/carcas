# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: MeetingNotes
def add_profiles_support(self):
    self.profiles = {}
    def register_profile(name, role="participant"):
        if name in self.profiles:
            raise ValueError(f"Profile '{name}' already exists")
        self.profiles[name] = {"role": role}
        return self
    def get_profile(name):
        return self.profiles.get(name) or None
    def list_profiles():
        return dict(self.profiles)
    add_profile = register_profile
    current_profile_name = "default"
    def use_profile(name):
        nonlocal current_profile_name
        profile = get_profile(name)
        if not profile:
            raise ValueError(f"Unknown profile '{name}'")
        self.current_profile_name = name
        return profile["role"]
    register_profile("admin", "admin")
    register_profile("default", "participant")
