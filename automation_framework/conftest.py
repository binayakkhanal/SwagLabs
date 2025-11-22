import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from automation_framework.core.config import Config
from automation_framework.core.logger import setup_logger
from datetime import datetime

logger = setup_logger()

@pytest.fixture(scope="function")
def driver(request):
    browser = Config.BROWSER
    headless = Config.HEADLESS
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    else:
        # Extend for other browsers if needed
        raise ValueError(f"Browser {browser} not supported")

    driver.maximize_window()
    driver.get(Config.BASE_URL)
    
    yield driver
    
    # Capture screenshot on failure
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"screenshots/failed_{request.node.name}_{timestamp}.png"
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        driver.save_screenshot(screenshot_name)
        logger.error(f"Test failed. Screenshot saved to {screenshot_name}")

    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def pytest_configure(config):
    config.option.htmlpath = "report.html"
