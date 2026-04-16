from pages.actions.login_actions import LoginActions
from pages.locators.login_locators import LoginLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = LoginActions(driver, base_url)
    
    
    def open_login_page(self, base_url):
        self.open(base_url)


    def login(self, username, password):
        self.actions.enter_username(username)
        self.actions.enter_password(password)
        self.actions.submit()