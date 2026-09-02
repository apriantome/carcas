# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: MeetingNotes
import sys

class AnsiColor:
    """ANSI color codes with enable/disable support."""
    _enabled = True
    _reset = '\033[0m'
    _codes = {
        'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m',
        'blue': '\033[34m', 'magenta': '\033[35m', 'cyan': '\033[36m',
        'white': '\033[37m', 'bold': '\033[1m', 'dim': '\033[2m',
    }

    @classmethod
    def disable(cls):
        cls._enabled = False

    @classmethod
    def enable(cls):
        cls._enabled = True

    @classmethod
    def color(cls, name, text):
        if not cls._enabled or name not in cls._codes:
            return text
        return cls._codes[name] + text + cls._reset

    @classmethod
    def red(cls, text): return cls.color('red', text)
    @classmethod
    def green(cls, text): return cls.color('green', text)
    @classmethod
    def yellow(cls, text): return cls.color('yellow', text)
    @classmethod
    def blue(cls, text): return cls.color('blue', text)
    @classmethod
    def bold(cls, text): return cls.color('bold', text)

def print_meeting_header(meeting):
    print(AnsiColor.bold(meeting['title']), file=sys.stderr)
    for k, v in meeting.items():
        if k != 'title' and v:
            print(f"  {AnsiColor.color('cyan', k)}: {v}", file=sys.stderr)
