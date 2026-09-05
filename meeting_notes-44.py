# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: MeetingNotes
import shutil
from datetime import datetime


def backup_data_file(data_file_path: str, backup_dir: str = "backups") -> str:
    """Creates a timestamped backup of the data file.

    Args:
        data_file_path: Path to the current data file.
        backup_dir: Directory to store backups in.

    Returns:
        The path to the created backup file.

    Raises:
        FileNotFoundError: If the data file does not exist.
    """
    if not os.path.exists(data_file_path):
        raise FileNotFoundError(f"Data file not found: {data_file_path}")

    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file_path = os.path.join(backup_dir, f"backup_{timestamp}_{os.path.basename(data_file_path)}")

    shutil.copy2(data_file_path, backup_file_path)
    return backup_file_path
