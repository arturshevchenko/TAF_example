import logging
import os

import pytest

from src.configs.config_loader import AppFolders

pytest_plugins = [
        "tests.fixtures.api_pets_fixtures",
        "tests.fixtures.browser_fixtures",
]


class NoColorFormatter(logging.Formatter):
    def format(self, record):
        message = super().format(record)

        # Remove ANSI escape codes (color codes)
        import re
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        message = ansi_escape.sub('', message)

        return message


@pytest.fixture(scope="session", autouse=True)
def configure_logging(request):
    # Create a file handler and set the log format
    logs_file_name = 'log.txt'
    logs_file_path = os.path.join(AppFolders.TMP_FILES_PATH, logs_file_name)
    if os.path.exists(logs_file_path):
        os.remove(logs_file_path)

    # Configure the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    yield

    # Clean up the logger
    root_logger.handlers.clear()


def issue_new(number=None):
    def decorator(func):
        func.issue_number = number
        return pytest.mark.issue_new(func)

    return decorator


def issue_fixed(number=None):
    def decorator(func):
        func.issue_number = number
        return pytest.mark.issue_fixed(func)

    return decorator


def smoke(func):
    return pytest.mark.smoke(func)


def regression(func):
    return pytest.mark.regression(func)


def positive(func):
    return pytest.mark.positive(func)


def negative(func):
    return pytest.mark.negative(func)


def web(func):
    return pytest.mark.web(func)


def api(func):
    return pytest.mark.app_api(func)


def sequential_group(func):
    return pytest.mark.sequential_group(func)


def parallel_group(func):
    return pytest.mark.parallel_group(func)


def serial(func):
    return pytest.mark.serial(func)
