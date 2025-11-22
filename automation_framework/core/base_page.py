from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from automation_framework.core.logger import setup_logger
from automation_framework.core.custom_waits import CustomWaits
import time

from automation_framework.core.config import Config

logger = setup_logger()

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)
        self.custom_waits = CustomWaits(driver, Config.TIMEOUT)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logger.info(f"Clicked on element: {locator}")
        except (TimeoutException, StaleElementReferenceException) as e:
            logger.error(f"Failed to click on element: {locator}. Error: {e}")
            raise

    def type(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logger.info(f"Typed '{text}' into element: {locator}")
        except Exception as e:
            logger.error(f"Failed to type into element: {locator}. Error: {e}")
            raise

    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            text = element.text
            logger.info(f"Got text '{text}' from element: {locator}")
            return text
        except Exception as e:
            logger.error(f"Failed to get text from element: {locator}. Error: {e}")
            raise

    def scroll_to(self, locator):
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            logger.info(f"Scrolled to element: {locator}")
        except Exception as e:
            logger.error(f"Failed to scroll to element: {locator}. Error: {e}")
            raise

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def js_click(self, locator):
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)
            logger.info(f"JS Clicked on element: {locator}")
        except Exception as e:
            logger.error(f"Failed to JS click on element: {locator}. Error: {e}")
            raise
