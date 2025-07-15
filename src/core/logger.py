import logging
import sys

_LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s - %(message)s"


def setup_logger(name: str | None = None, level: int = logging.INFO) -> logging.Logger:
    """Creates a pre-configured logger with the specified name."""

    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(_LOG_FORMAT)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Add cloud handlers if necessary

    return logger
