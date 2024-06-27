from selene import Browser


class BasePage:
    body = 'body'

    def __init__(self, browser: Browser):
        self.browser = browser

    def get_title(self):
        return self.browser.driver.title

    def get_body(self):
        return self.browser.element(self.body)
