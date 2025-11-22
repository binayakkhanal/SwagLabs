import requests
from automation_framework.core.config import Config
from automation_framework.core.logger import setup_logger

logger = setup_logger()

class APIClient:
    def __init__(self):
        self.base_url = Config.API_BASE_URL

    def get_users(self):
        url = f"{self.base_url}/users"
        response = requests.get(url)
        logger.info(f"GET {url} - Status: {response.status_code}")
        return response

    def create_post(self, title, body, user_id):
        url = f"{self.base_url}/posts"
        payload = {"title": title, "body": body, "userId": user_id}
        response = requests.post(url, json=payload)
        logger.info(f"POST {url} - Status: {response.status_code}")
        return response
