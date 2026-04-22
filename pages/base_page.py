from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys 

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        self.driver.get(base_url)

    def click(self, locator):
        action = self.wait.until(EC.element_to_be_clickable(locator))
        action.click()

    def delete_text(self, locator):
        action = self.wait.until(EC.element_to_be_clickable(locator))
        action.click()
        action.send_keys(Keys.SHIFT + Keys.HOME)
        action.send_keys(Keys.DELETE)

    def enter_text(self, locator, text):
        action = self.wait.until(EC.visibility_of_element_located(locator))
        action.clear()
        action.send_keys(text)

    def text_of_element(self, locator):
        action = self.wait.until(EC.visibility_of_element_located(locator))
        return action.text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_presence(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def find_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element