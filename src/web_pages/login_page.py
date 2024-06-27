import allure
from selenium.webdriver.common.by import By
from web_pages.base_page import BasePage

from src.configs.urls import Urls


class LoginPage(BasePage):
    _email_field = (By.XPATH, "(//input[@name='email'])[2]")
    _sign_in_btn = (By.XPATH, "(//input[@name='sign_in'])[2]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Open page")
    def open_page(self):
        self.open_url(str(Urls.login_url.value))
        return self

    @allure.step("Fill email: {0}")
    def fill_email(self, email: str):
        self.fill_text_field(self._email_field, email)
        return self

    @allure.step("Click Sign In")
    def click_sign_in(self):
        sign_in_button = self.wait.until_element_presence(self._sign_in_btn)
        sign_in_button.click()
        return self

    @allure.step("Log in with email:{} password:{}")
    def login_with(self, email: str, password: str):
        self.fill_email(email).fill_password(password).click_sign_in()
