from pages.actions.login_actions import LoginActions
from pages.base_page import BasePage
from pages.locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = LoginActions(driver, base_url)
    
    def login(self, username, password):
        self.actions.enter_username(username)
        self.actions.enter_password(password)
        self.actions.submit()

    def find_lock_icon(self):
        return self.is_visible(LoginLocators.LOCK_ICON)