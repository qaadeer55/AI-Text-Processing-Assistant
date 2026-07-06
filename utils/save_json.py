import json

from pathlib import Path
from datetime import datetime


def save_json(data, filename):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    name = f"{timestamp}_{filename}"

    output_path = Path("outputs") / name

    with open(output_path, "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4)

    return output_path