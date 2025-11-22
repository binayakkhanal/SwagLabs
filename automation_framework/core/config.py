import os

class Config:
    BASE_URL = "https://www.saucedemo.com"
    API_BASE_URL = "https://jsonplaceholder.typicode.com"
    TIMEOUT = 30
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    BROWSER = os.getenv("BROWSER", "chrome")
