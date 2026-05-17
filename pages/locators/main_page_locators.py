from selenium.webdriver.common.by import By


class MainPageLocators:
    TITLE = (By.ID, 'react-admin-title')
    PROFILE_BUTTON = (By.XPATH, '//button[@aria-label="Profile"]')
    LOG_OUT_ICON = (By.CSS_SELECTOR, '[data-testid="PowerSettingsNewIcon"]')
    USERS_BUTTON = (By.XPATH, '//a[@role="menuitem" and contains(text(), "Users")]')
    STATUSES_BUTTON = (By.XPATH, '//a[@role="menuitem" and contains(text(), "Task statuses")]')
    LABELS_BUTTON = (By.XPATH, '//a[@role="menuitem" and contains(text(), "Labels")]')
    TASKS_BUTTON = (By.XPATH, '//a[@role="menuitem" and contains(text(), "Tasks")]')
    DASHBOARD_BUTTON = (By.XPATH, '//a[@role="menuitem" and contains(text(), "Dashboard")]')
    DASHBOARD_CARD = (By.CSS_SELECTOR, ".MuiCardContent-root")
    DASHBOARD_CARD_TEXT = "Lorem ipsum sic dolor amet..."

    @staticmethod
    def nav_item_by_name(name):
        return By.XPATH, f"//a[@role='menuitem'][contains(., '{name}')]"