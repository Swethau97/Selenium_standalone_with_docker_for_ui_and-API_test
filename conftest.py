import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SingletonDriverInstance:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            selenium_url = os.getenv("SELENIUM_URL")

            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")

            if selenium_url:
                print(f"✅ Running in Docker - connecting to remote Selenium at {selenium_url}")
                cls._instance = webdriver.Remote(
                    command_executor=selenium_url,
                    options=chrome_options
                )
            else:
                print("✅ Running locally - using local ChromeDriver")
                cls._instance = webdriver.Chrome(options=chrome_options)

        return cls._instance


@pytest.fixture(scope="session")
def driver():
    driver = SingletonDriverInstance()
    yield driver
    driver.quit()
