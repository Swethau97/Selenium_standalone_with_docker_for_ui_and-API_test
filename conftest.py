#Initializing a singleton driver instance
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Utils.Logger import initialize_logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import webdriver_manager
class SingletonDriverinstance:
    _isinstance=None
    def __new__(cls, *args, **kwargs):
        if cls._isinstance is None:
            chrome_option=Options()
            chrome_option.add_argument('--start-maximized')
            service=Service(ChromeDriverManager().install())
            cls._isinstance=webdriver.Chrome(service=service,options=chrome_option)
            return cls._isinstance
    @classmethod
    def quit_session(cls):
        if cls._isinstance:
            cls._isinstance.quit()
            cls._isinstance=None

@pytest.fixture(scope="session")
def driver():
    driver=SingletonDriverinstance()
    yield driver
    SingletonDriverinstance.quit_session()