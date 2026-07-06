from pathlib import Path
from datetime import datetime


def save_text(content, filename):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    name = f"{timestamp}_{filename}"

    output_path = Path("outputs") / name

    output_path.write_text(content, encoding="utf-8")

    return output_path