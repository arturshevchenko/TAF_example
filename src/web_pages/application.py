from web_pages.login_page import LoginPage


class Application:

    def __init__(self, driver):
        self.driver = driver

    def login_page(self):
        return LoginPage(self.driver)
