import logging
from pathlib import Path


LOG_DIRECTORY = Path("logs")
LOG_DIRECTORY.mkdir(exist_ok=True)

LOG_FILE = LOG_DIRECTORY / "application.log"


logger = logging.getLogger("AI_Text_Processing_Assistant")

logger.setLevel(logging.DEBUG)


if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )

    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)