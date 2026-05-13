from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    LOCK_ICON = (By.CSS_SELECTOR, '[data-testid="LockIcon"]')