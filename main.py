import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click();
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click();
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click();
time.sleep(3)
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click();


price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

total_price = 0.0

for price_el in price_elements:
    price_text = price_el.text.strip()   # e.g. "$29.99"
    price_value = float(price_text.replace("$", ""))  # convert to float
    total_price += price_value

print("Calculated Total:", total_price)
