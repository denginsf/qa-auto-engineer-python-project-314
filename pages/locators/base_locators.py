from selenium.webdriver.common.by import By


class BaseLocators:
    CREATE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Create"]')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit" and contains(text(), "Save")]')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Delete"]')
    SELECT_ALL = (By.CSS_SELECTOR, '.select-all')
    FORM = (By.CSS_SELECTOR, '.MuiStack-root')
    SUCCESS_SNACKBAR = (By.XPATH, '//div[text()="Element created"]')
    ERROR_SNACKBAR = (By.XPATH, '//div[text()="The form is not valid. Please check for errors"]')
    UPDATED_SNACKBAR = (By.XPATH, '//div[text()="Element updated"]')
    DELETED_SNACKBAR = (By.XPATH, '//div[text()="Element deleted"]')
    ALL_DELETED_SNACKBAR = (By.XPATH, '//div[contains(text(), "elements deleted")]')
    REQUIRED_ERROR = (By.XPATH, '//p[text()="Required"]')