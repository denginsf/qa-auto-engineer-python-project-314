from pages.actions.main_page_actions import MainPageActions
from pages.locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = MainPageActions(driver, base_url)
    
    
    def title(self):
        return self.actions.get_title()

    def logout(self):
        self.actions.click_on_profile()
        self.actions.click_on_logout()