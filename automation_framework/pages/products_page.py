from selenium.webdriver.common.by import By
from automation_framework.core.base_page import BasePage
import random

class ProductsPage(BasePage):
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.XPATH, ".//button[contains(text(), 'Add to cart')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_random_products_to_cart(self, count=3):
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        selected_products = random.sample(products, min(count, len(products)))
        
        for product in selected_products:
            add_button = product.find_element(*self.ADD_TO_CART_BUTTON)
            add_button.click()

    def get_cart_count(self):
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_LINK)
