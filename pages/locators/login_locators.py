from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN = (By.ID, ":r6:")
    PASSWORD = (By.ID, ":r4:")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/form/div/button')
    LOCK_ICON = (By.CSS_SELECTOR, '[data-testid="LockIcon"]')