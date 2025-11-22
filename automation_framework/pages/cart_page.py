from selenium.webdriver.common.by import By
from automation_framework.core.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_total_price(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        total = 0.0
        for item in items:
            price_text = item.find_element(*self.ITEM_PRICE).text
            price = float(price_text.replace("$", ""))
            total += price
        return total

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
