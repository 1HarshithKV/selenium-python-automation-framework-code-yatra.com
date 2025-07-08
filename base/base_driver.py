"""
Here we are keeping the commonly used codes, so that same code we can use in the different tests also
"""

from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def page_scroll(self):
        self.driver.execute_script("window.scrollBy(0,900)")
        sleep(2)
        self.driver.execute_script("window.scrollTo(900,0)")
        sleep(2)

    def wait_for_presence_of_all_element(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 40)
        list_of_elements = wait.until(EC.presence_of_element_located(locator_type, locator))
        return list_of_elements

    def wait_until_element_is_clickable(self,locator_type,locator):
        element = self.driver.find_element(locator_type,locator)
        return element


