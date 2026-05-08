from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


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
        action = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Create"]')))
        action.click()

    def open_entity_creation_form(self):
        self.start_entity_creation()
        return self.is_visible((By.CSS_SELECTOR, '.MuiStack-root'))

    def save_entity(self):
        action = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(text(), "Save")]')))
        action.click()

    def delete_entity(self):
        action = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Delete"]')))
        action.click()

    def select_all_entitys(self):
        action = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.select-all')))
        action.click()

    def find_succes_snackbar(self):
        return self.is_visible((By.XPATH, '//div[text()="Element created"]'))

    def find_error_snackbar(self):
        return self.is_visible((By.XPATH, '//div[text()="The form is not valid. Please check for errors"]'))
    
    def find_updated_snackbar(self):
        return self.is_visible((By.XPATH, '//div[text()="Element updated"]'))

    def find_deleted_snackbar(self):
        return self.is_visible((By.XPATH, '//div[text()="Element deleted"]'))
    
    def find_all_entitys_deleted_snackbar(self):
        return self.is_visible((By.XPATH, '//div[contains(text(), "elements deleted")]'))

    def get_required_errors_count(self):        
        return len(self.driver.find_elements(By.XPATH, '//p[text()="Required"]'))
    
    def find_in_element(self, element, locator):
        return element.find_element(*locator)