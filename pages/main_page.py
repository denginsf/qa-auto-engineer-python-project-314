from pages.actions.main_page_actions import MainPageActions
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = MainPageActions(driver, base_url)
    
    
    def title(self):
        return self.actions.get_title()


    def logout(self):
        self.actions.logout()


    def go_to_users(self):
        self.actions.click_on_users()


    def go_to_statuses(self):
        self.actions.click_on_statuses()


    def go_to_labels(self):
        self.actions.click_on_labels()


    def go_to_tasks(self):
        self.actions.click_on_tasks()

    def all_nav_items_visible_and_clickable(self):
        return self.actions.all_nav_items_visible_and_clickable()

    def dashboard_card_is_correct(self):
        return (self.actions.dashboard_card_is_visible() and
                self.actions.dashboard_card_text_is_correct())