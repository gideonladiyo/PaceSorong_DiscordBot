import os

class Path:
    BASE_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

    RENUNGAN_PATH = os.path.join(BASE_DIR, "data", "renungan_channel.json")

file_path = Path()