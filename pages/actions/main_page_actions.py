from pages.locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPageActions(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
    
    def get_title(self):
        return self.text_of_element(MainPageLocators.TITLE)