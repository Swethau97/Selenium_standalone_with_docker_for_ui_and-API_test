from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseMethods:
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,by_and_value,timeout=20):
        element= WebDriverWait(self.driver,timeout).until(presence_of_element_located((by_and_value)))
        return element

    def find_elements(self,by_and_value,timeout=15):
        elements=WebDriverWait(self.driver,15).until(presence_of_all_elements_located((by_and_value)))
        return elements

    def send_keys(self,by_and_value,text_to_be_entered,timeout=15):
        element=self.find_element(by_and_value,timeout)
        element.clear()
        element.send_keys(text_to_be_entered)
    def click(self,by_and_value,timeout=15):
        element=self.find_element(by_and_value,timeout)
        element.click()

    def scroll_by_element(self, by_and_value, timeout=15):
        element = self.find_element(by_and_value, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    def scroll_by_pixels(self):
        self.driver.execute_script("window.scrollBy(0, 500);")




