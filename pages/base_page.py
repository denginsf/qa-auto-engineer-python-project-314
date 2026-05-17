from pages.locators.base_locators import BaseLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

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


    def js_click(self, locator):
        action = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", action)


    def esc(self):
         ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()


    def delete_text(self, locator):
        action = self.wait.until(EC.element_to_be_clickable(locator))
        action.click()
        action.send_keys(Keys.SHIFT + Keys.HOME)
        action.send_keys(Keys.DELETE)


    def enter_text(self, locator, text):
        action = self.wait.until(EC.visibility_of_element_located(locator))
        action.click()
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


    def find_elements(self, locator):
        return self.driver.find_elements(*locator)


    def start_entity_creation(self):
        action = self.wait.until(EC.element_to_be_clickable(BaseLocators.CREATE_BUTTON))
        action.click()


    def open_entity_creation_form(self):
        self.start_entity_creation()
        return self.is_visible(BaseLocators.FORM)


    def save_entity(self):
        action = self.wait.until(EC.element_to_be_clickable(BaseLocators.SAVE_BUTTON))
        action.click()


    def delete_entity(self):
        action = self.wait.until(EC.element_to_be_clickable(BaseLocators.DELETE_BUTTON))
        action.click()


    def select_all_entities(self):
        action = self.wait.until(EC.element_to_be_clickable(BaseLocators.SELECT_ALL))
        action.click()


    def find_success_snackbar(self):
        return self.is_visible(BaseLocators.SUCCESS_SNACKBAR)


    def find_error_snackbar(self):
        return self.is_visible(BaseLocators.ERROR_SNACKBAR)
    

    def find_updated_snackbar(self):
        return self.is_visible(BaseLocators.UPDATED_SNACKBAR)


    def find_deleted_snackbar(self):
        return self.is_visible(BaseLocators.DELETED_SNACKBAR)
    

    def find_all_entities_deleted_snackbar(self):
        return self.is_visible(BaseLocators.ALL_DELETED_SNACKBAR)


    def get_required_errors_count(self):        
        return len(self.driver.find_elements(*BaseLocators.REQUIRED_ERROR))
    

    def find_in_element(self, element, locator):
        return element.find_element(*locator)
    

    def is_clickable_in_element(self, parent, locator):
        try:
            element = parent.find_element(*locator)
            return element.is_enabled() and element.is_displayed()
        except NoSuchElementException:
            return False
        
        
    def is_save_button_disabled(self):
        button = self.find_element(BaseLocators.SAVE_BUTTON)
        return button.get_attribute('disabled') is not None
    
    
    def is_clickable(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False


    def wait_for_count_stable(self, locator, previous_count):
        self.wait.until(lambda d: len(d.find_elements(*locator)) != previous_count)
        time.sleep(0.3)
        count = len(self.driver.find_elements(*locator))
        self.wait.until(lambda d: len(d.find_elements(*locator)) == count)

    
    def get_page_title(self):
        return self.text_of_element(BaseLocators.TITLE)


    def is_on_page(self, expected_title):
        return self.get_page_title() == expected_title


    def is_on_page_by_url(self, expected_url_part):
        return expected_url_part in self.driver.current_url
    

    def browser_title_is_correct(self):
        return self.driver.title == 'Task manager'