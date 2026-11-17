import logging
import os
from logging.handlers import RotatingFileHandler


os.makedirs("reports", exist_ok=True)

logger = logging.getLogger("automation")
logger.setLevel(logging.INFO)

if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        "reports/automation.log",
        maxBytes=1024 * 1024,
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


def get_logger(name):
    return logging.getLogger(f"automation.{name}")