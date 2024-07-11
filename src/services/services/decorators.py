import logging

from src.configs.colors import Colors
from src.configs.config_loader import AppConfigs


def service_logger(func):
    def wrapper(*args, **kwargs):
        if AppConfigs.LOGS:
            logging.info(
                f"{Colors.Red}\n{'-' * 50}\n\n{func.__name__}\n{Colors.Reset}".upper()
            )
        return func(*args, **kwargs)

    return wrapper


def service_logger_text(text):
    def inner_logger(func):
        def wrapper(*args, **kwargs):
            if AppConfigs.LOGS:
                logging.info(
                    f"{Colors.Red}\n{'-' * 50}\n\n{text}\n{Colors.Reset}".upper()
                )
            return func(*args, **kwargs)

        return wrapper

    return inner_logger
