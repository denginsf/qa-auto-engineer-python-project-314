from selenium.webdriver.common.by import By

class StatusesLocators:
    CREATE_STATUS_BUTTON = (By.CSS_SELECTOR, '[aria-label="Create"]')
    USER_CREATION_FORM = (By.CSS_SELECTOR, '.MuiStack-root')
    STATUS_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    STATUS_SLUG_INPUT = (By.CSS_SELECTOR, 'input[name="slug"]')
    STATUS_HEADER_CHECK_BOX = (By.CSS_SELECTOR, '.select-all input')
    STATUS_ID_COLUMN = (By.CSS_SELECTOR, '[data-field="id"]')
    NAME_COLUMN = (By.CSS_SELECTOR, '[data-field="name"]')
    SLUG_COLUMN = (By.CSS_SELECTOR, '.column-slug span')
    
    @staticmethod
    def get_row_by_status_name(name):
        return (By.XPATH, f'//td[contains(@class, "column-name")]//span[text()="{name}"]/ancestor::tr')