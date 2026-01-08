from __future__ import annotations
import logging
from datetime import datetime
from pathlib import Path

def ensure_dir(path: str | Path) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

def setup_logger(logs_dir: str | Path) -> logging.Logger:
    ensure_dir(logs_dir)
    logger = logging.getLogger("pipeline")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = Path(logs_dir) / f"run_{ts}.log"

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.info(f"Logging to: {log_path}")
    return logger
