from pages.actions.statuses_actions import StatusesActions
from pages.locators.statuses_locators import StatusesLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException

class StatusesPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = StatusesActions(driver, base_url)


    def input_status_data(self, name, slug):
        self.actions.enter_status_name(name)
        self.actions.enter_status_slug(slug)
        self.save_entity()


    def delete_status_name(self):
        self.actions.delete_status_name()


    def delete_status_slug(self):
        self.actions.delete_status_slug()


    def get_status_data_by_name(self, name):
        return self.actions.find_status_data_by_name_column(name)


    def get_all_statuses_data(self):
        return self.actions.find_all_status_data()
    
    
    def statuses_table_is_loaded(self):
        columns_visible = all([
            self.is_presence(StatusesLocators.STATUS_HEADER_CHECK_BOX),
            self.is_clickable(StatusesLocators.STATUS_ID_COLUMN),
            self.is_clickable(StatusesLocators.NAME_COLUMN),
            self.is_clickable(StatusesLocators.SLUG_COLUMN),
            self.is_clickable(StatusesLocators.CREATED_AT_COLUMN)
        ]
        )
        return columns_visible


    def statuses_table_is_empty(self):
        empty_table = all([
            self.is_visible(StatusesLocators.STATUSES_EMPTY_STATE),
            self.is_visible(StatusesLocators.STATUSES_EMPTY_STATE_ICON),
            self.is_visible(StatusesLocators.STATUSES_EMPTY_STATE_TITLE),
            self.is_visible(StatusesLocators.STATUSES_EMPTY_STATE_TEXT),
            self.is_visible(StatusesLocators.CREATE_STATUS_BUTTON)
        ])
        return empty_table
    

    def click_on_status_row(self, name):
        self.find_element(StatusesLocators.get_row_by_status_name(name)).click()


    def is_status_exist(self, name):
        try:
            self.find_element(StatusesLocators.get_row_by_status_name(name))
            return True
        except TimeoutException:
            return False