from selene import Browser

from src.configs.urls import Urls
from src.page_objects.BasePage import BasePage


class HomePage(BasePage):
    search_textarea_locator = "//*[@id='docsearch-0']/button"

    def __init__(self, browser: Browser):
        super().__init__(browser)

    def open_page(self):
        self.browser.open(Urls.root_url.value)
        return self
