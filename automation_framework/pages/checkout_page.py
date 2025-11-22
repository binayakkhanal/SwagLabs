from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from automation_framework.core.base_page import BasePage
from automation_framework.core.logger import setup_logger

logger = setup_logger()

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_information(self, first_name, last_name, postal_code):
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        self.scroll_to(self.FIRST_NAME_INPUT)
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)
        self.js_click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        self.scroll_to(self.FINISH_BUTTON)
        self.js_click(self.FINISH_BUTTON)

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)
