import requests

from scraper.config import BASE_URL
from scraper.logger import logger


def fetch_page():

    logger.info("Fetching Website...")

    response = requests.get(BASE_URL)

    logger.info(f"Status Code: {response.status_code}")

    return response.text