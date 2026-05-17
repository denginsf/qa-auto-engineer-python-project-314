from pages.base_page import BasePage
from pages.locators.main_page_locators import MainPageLocators


class MainPageActions(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def get_title(self):
        return self.text_of_element(MainPageLocators.TITLE)

    def logout(self):
        self.click(MainPageLocators.PROFILE_BUTTON)
        self.click(MainPageLocators.LOG_OUT_ICON)

    def click_on_users(self):
        self.click(MainPageLocators.USERS_BUTTON)

    def click_on_statuses(self):
        self.click(MainPageLocators.STATUSES_BUTTON)

    def click_on_labels(self):
        self.click(MainPageLocators.LABELS_BUTTON)

    def click_on_tasks(self):
        self.click(MainPageLocators.TASKS_BUTTON)

    def all_nav_items_visible_and_clickable(self):
        nav_items = ['Dashboard', 'Tasks', 'Users', 'Labels', 'Task statuses']
        return all(
            self.is_clickable(MainPageLocators.nav_item_by_name(item))
            for item in nav_items
        )

    def dashboard_card_is_visible(self):
        return self.is_visible(MainPageLocators.DASHBOARD_CARD)

    def dashboard_card_text_is_correct(self):
        return self.text_of_element(MainPageLocators.DASHBOARD_CARD) == MainPageLocators.DASHBOARD_CARD_TEXT