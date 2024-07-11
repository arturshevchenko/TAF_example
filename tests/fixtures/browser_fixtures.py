import pytest
from selene import Browser, Config
from selenium import webdriver

from src.configs.config_loader import AppConfigs
from src.page_objects.app import Application


@pytest.fixture(scope="session")
def browser():
    browser = Browser(
        Config(
            driver=get_browser(),
            base_url=AppConfigs.BASE_URL,
            timeout=4,
            window_width=1200,
            window_height=800,
        )
    )

    yield browser

    browser.close()


def get_browser():
    if AppConfigs.WEB_DRIVER == "CHROME":
        return webdriver.Chrome()
    elif AppConfigs.WEB_DRIVER == "FIREFOX":
        return webdriver.Firefox()


@pytest.fixture(scope="session")
def app(browser):
    return Application(browser)
