from BasePages.Basemethods import BaseMethods
from selenium.webdriver.common.by import By

class Login_page(BaseMethods):
    # Class variables for locators (static, shared across all instances)
    USERNAME_LOCATOR = (By.ID, "userName")
    PASSWORD_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "login")

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BaseMethods with driver

    def login(self, username, password):
        # Use inherited methods from BaseMethods
        self.send_keys(self.USERNAME_LOCATOR, username)
        self.send_keys(self.PASSWORD_LOCATOR, password)
        self.click(self.LOGIN_BUTTON_LOCATOR)

    def scroll_in_the_login(self):
        self.scroll_by_element(self.LOGIN_BUTTON_LOCATOR)



