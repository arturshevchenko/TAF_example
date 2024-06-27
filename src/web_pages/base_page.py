from dataclasses import dataclass

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from web_pages.waits import Waits

from src.configs.config_loader import AppConfigs


@dataclass
class BasePage:
    """
    BasePage should contain all common site-page functionality
    """
    # constructor
    driver: WebDriver
    # additional
    _form_title = (By.XPATH, "//h2[contains(@class, 'FormLayout__title')]")
    _title_locator = (By.XPATH, "//*[@data-qa='qa-title']")
    _subtitle_locator = (By.XPATH, "//*[@data-qa='qa-subtitle']")

    _loader = (By.XPATH, "//div[contains(@class,'MuiCircularProgress')]")

    @property
    def wait(self):
        """
        Init class Waits(selenium waits).
        (e.g: self.wait.until....)
        :return:
        """
        return Waits(self.driver)

    def open_url(self, url: str):
        self.driver.get(AppConfigs.BASE_URL + url)
        return self

    def is_element_visible(self, element):
        try:
            WebDriverWait(
                    self.driver,
                    AppConfigs.UI_MAX_RESPONSE_TIME
            ).until(expected_conditions.presence_of_element_located(element))
            return True
        finally:
            return False

    def scroll_to_top(self):
        self.driver.find_elements(By.ID, "app")[0].send_keys(Keys.HOME)
        return self

    def scroll_to_element(self, _element_locator):
        element = self.driver.find_element(_element_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def get_text(self, _element_locator):
        element = self.wait.until_element_presence(_element_locator)
        return element.text

    def get_value(self, _element_locator):
        element = self.wait.until_element_presence(_element_locator)
        return element.get_attribute("value")

    def hover(self, element):
        hov = ActionChains(self.driver).move_to_element(element)
        hov.perform()

    def page_title(self):
        return self.get_text(self._title_locator)

    def page_subtitle(self):
        return self.get_text(self._subtitle_locator)

    def get_form_title(self):
        return self.get_text(self._form_title)

    def fill_text_field(self, locator, text: str):
        field = self.wait.until_element_presence(locator)
        field.clear()
        # if platform.system() == 'Darwin':
        #     # time.sleep(1)
        #     ActionChains(self.driver).click(field).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
        # else:
        #     ActionChains(self.driver).click(field).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        # ActionChains(self.driver).send_keys(Keys.BACKSPACE).perform()
        field.send_keys(text)
        return self

    def click_checkbox_field(self, locator):
        field = self.wait.until_element_presence(locator)
        field.click()
        return self

    def wait_till_loader_is_hidden(self):
        self.wait.until_element_dissapears(self._loader)
        return self

    def is_disabled(self, locator):
        field = self.wait.until_element_presence(locator)
        return field.get_attribute("disabled")
