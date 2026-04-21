from selenium.webdriver.common.by import By

class MainPageLocators:
    TITLE = (By.ID, 'react-admin-title')
    PROFILE_BUTTON = (By.XPATH, '//button[@aria-label="Profile"]')
    LOG_OUT_BUTTON = (By.CSS_SELECTOR, '[data-testid="PowerSettingsNewIcon"]')
    USERS_BUTTON = (By.XPATH, '//a[@role="menuitem" and contains(text(), "Users")]')