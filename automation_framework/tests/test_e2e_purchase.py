import pytest
from automation_framework.pages.login_page import LoginPage
from automation_framework.pages.products_page import ProductsPage
from automation_framework.pages.cart_page import CartPage
from automation_framework.pages.checkout_page import CheckoutPage
from automation_framework.core.logger import setup_logger

logger = setup_logger()

def test_e2e_purchase(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    logger.info("Starting E2E Purchase Test")

    # 1. Login
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Add 3 random products to cart
    products_page.add_random_products_to_cart(3)
    assert products_page.get_cart_count() == 3
    
    # 3. Go to cart
    products_page.go_to_cart()
    
    # 4. Validate total price
    total_price = cart_page.get_total_price()
    logger.info(f"Total price calculated: {total_price}")
    assert total_price > 0
    
    # 5. Checkout
    cart_page.proceed_to_checkout()
    
    # 6. Fill information
    checkout_page.fill_information("John", "Doe", "12345")
    
    # 7. Finish checkout
    checkout_page.finish_checkout()
    
    # 8. Verify Finish page
    message = checkout_page.get_complete_message()
    assert "Thank you for your order!" in message
    
    logger.info("E2E Purchase Test Completed Successfully")
