from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomWaits:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_until_page_load(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def wait_until_ajax_complete(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script("return jQuery.active == 0") if d.execute_script("return typeof jQuery != 'undefined'") else True
        )
