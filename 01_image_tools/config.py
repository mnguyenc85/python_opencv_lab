from pathlib import Path

# Thư mục gốc project
BASE_DIR = Path(__file__).resolve().parent

# Database
DATA_DIR = BASE_DIR / "data"
CAPTURE_DIR = BASE_DIR / "captures"
SETTINGS_DIR = CAPTURE_DIR / "settings.db"