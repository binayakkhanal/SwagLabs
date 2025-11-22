import pytest
import json
import os
from automation_framework.pages.login_page import LoginPage
from automation_framework.pages.products_page import ProductsPage

def load_login_data():
    data_path = os.path.join(os.path.dirname(__file__), "../data/login_test_data.json")
    with open(data_path, 'r') as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_login_data())
def test_data_driven_login(driver, data):
    login_page = LoginPage(driver)
    
    login_page.login(data["username"], data["password"])
    
    if data["expected_result"] == "success":
        # Check if login was successful by looking for an element on the products page
        # For simplicity, we can check URL or an element
        assert "inventory.html" in driver.current_url
    else:
        error_message = login_page.get_error_message()
        assert data["error_message"] in error_message
