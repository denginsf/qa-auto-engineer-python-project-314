from pages.locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginActions(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def enter_username(self, username):
        self.enter_text(LoginLocators.LOGIN, username)

    def enter_password(self, password):
        self.enter_text(LoginLocators.PASSWORD, password)

    def submit(self):
        self.click(LoginLocators.LOGIN_BUTTON)