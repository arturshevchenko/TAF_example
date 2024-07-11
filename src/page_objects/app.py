from selene import Browser

from src.page_objects.HomePage import HomePage


class Application:
    def __init__(self, browser: Browser):
        self.browser = browser

    def home_page(self):
        return HomePage(self.browser)
