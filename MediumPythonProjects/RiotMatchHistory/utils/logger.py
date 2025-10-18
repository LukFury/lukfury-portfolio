import logging
from datetime import datetime
from pathlib import Path

def get_logger(name: str = "riot_logger", log_dir: Path | None = None) -> logging.Logger:
    """
    Create and configure a logger with both console and file output.
    If log_dir isn't given, it defaults to <project_root>/logs.
    """
    # Automatically resolve to project root (2 levels above utils/)
    if log_dir is None:
        log_dir = Path(__file__).resolve().parents[2] / "logs"

    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{datetime.now():%Y-%m-%d}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        ))

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s]: %(message)s", "%H:%M:%S"
        ))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
