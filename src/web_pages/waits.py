import logging

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.configs.config_loader import AppConfigs


class Waits:
    def __init__(self, driver):
        self.driver = driver
        self.wait_element = WebDriverWait(
            driver,
            AppConfigs.UI_MAX_RESPONSE_TIME,
            ignored_exceptions=WebDriverException,
        )

    def until_element_presence(self, element, message=None):
        """
        wait until test_web element/elements appears in DOM with delay of 0,5 second,
        in case if elements/element is present returns test_web element/elements else throws exception
        @param element: (By.*locator_type*, "locator")
        @param message: Assertion message
        @return: test_web element
        """
        return self.wait_element.until(
            expected_conditions.presence_of_element_located(element), message
        )

    def until_elements_presence(self, elements, message=None):
        """
        wait until test_web element/elements appears in DOM with delay of 0,5 second,
        in case if elements/element is present returns test_web element/elements else throws exception
        @param elements: (By.*locator_type*, "locator")
        @param message: Assertion message
        @return: test_web element
        """
        return self.wait_element.until(
            expected_conditions.presence_of_all_elements_located(elements), message
        )

    def until_element_dissapears(self, element, message=None):
        """
        wait until test_web element/elements disappears in DOM with delay of 0,5 second,
        in case if elements/element is present returns test_web element/elements else throws exception
        @param element: (By.*locator_type*, "locator")
        @param message: Assertion message
        @return: test_web element
        """
        return self.wait_element.until(
            expected_conditions.invisibility_of_element_located(element), message
        )

    def until_elements_presence_by_xpath(self, element, message=None):
        """
        wait until test_web element/elements appears in DOM with delay of 0,5 second,
        in case if elements/element is present returns test_web element/elements else throws exception
        @param element: XPATH
        @param message: Assertion message
        @return: test_web element/elements
        """
        logging.info(f"Looking for xpath: {element}")
        return self.wait_element.until(
            expected_conditions.presence_of_all_elements_located((By.XPATH, element)),
            message,
        )

    def until_element_visible_by_id(self, element, message=None):
        """
        wait until test_web element/elements if visible with delay 0,5 second by default
        @param element: ID
        @param message: Assertion message
        @return: test_web element/elements else False
        """
        logging.info(f"Looking for id: {element}")
        return self.wait_element.until(
            expected_conditions.visibility_of_element_located((By.ID, element)), message
        )

    def until_element_presence_by_xpath(self, element, message=None):
        """
        wait until test_web element appears in DOM with delay of 0,5 second,
        in case if element is present returns test_web element else throws exception
        @param element: XPATH
        @param message: Assertion message
        @return: test_web element
        """
        logging.info(f"Looking for xpath: {element}")
        return self.wait_element.until(
            expected_conditions.presence_of_element_located((By.XPATH, element)),
            message,
        )

    def until_element_visible_by_class_name(self, element, message=None):
        """
        wait until test_web element/elements if visible with delay 0,5 second by default
        @param element: CLASS_NAME
        @param message: Assertion message
        @return: test_web element/elements else False
        """
        logging.info(f"Looking for class_name: {element}")
        return self.wait_element.until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, element)),
            message,
        )

    def until_element_visible_by_xpath(self, element, message=None):
        """
        wait until test_web element/elements is visible
        @param element: XPATH
        @param message: Assertion message
        @return: test_web element/elements else False
        """
        logging.info(f"Looking for xpath: {element}")
        return self.wait_element.until(
            expected_conditions.visibility_of_element_located((By.XPATH, element)),
            message,
        )

    def until_elements_visible_by_class_name(self, element, message=None):
        """
        wait until test_web element/elements appears in DOM with delay of 0,5 second,
        in case if elements/element is visible returns test_web element/elements else throws exception
        @param element: CLASS NAME
        @param message: Assertion message
        @return: test_web element/elements
        """
        logging.info(f"Looking for class_name: {element}")
        return self.wait_element.until(
            expected_conditions.presence_of_all_elements_located(
                (By.CLASS_NAME, element)
            ),
            message,
        )

    def until_elements_visible_by_xpath(self, element, message=None):
        """
        wait until test_web element/elements appears in DOM with delay of 0,5 second,
        in case if elements/element is visible returns test_web element/elements else throws exception
        @param element: XPATH
        @param message: Assertion message
        @return: test_web element/elements
        """
        logging.info(f"Looking for xpath: {element}")
        return self.wait_element.until(
            expected_conditions.visibility_of_any_elements_located((By.XPATH, element)),
            message,
        )

    def until_element_not_visible_by_xpath(self, element, message=None):
        """
        wait until test_web element/elements is not visible
        @param element: XPATH
        @param message: Assertion message
        @return: test_web element/elements else False
        """
        logging.info(f"Looking for xpath: {element}")
        return self.wait_element.until(
            expected_conditions.invisibility_of_element_located((By.XPATH, element)),
            message,
        )
