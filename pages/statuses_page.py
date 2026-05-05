from pages.actions.statuses_actions import StatusesActions
from pages.locators.statuses_locators import StatusesLocators
from pages.base_page import BasePage

class StatusesPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = StatusesActions(driver, base_url)

    def open_status_creation_form(self):
        self.actions.start_status_creation()
        return self.is_visible(StatusesLocators.USER_CREATION_FORM)

    def input_status_data(self, name, slug):
        self.actions.enter_status_name(name)
        self.actions.enter_status_slug(slug)
        self.save_entity()

    def get_status_data_by_name(self, name):
        return self.actions.find_status_data_by_name_colum(name)

    
    def statuses_table_is_loaded(self):
        columns_visible = all([
            self.is_presence(StatusesLocators.STATUS_HEADER_CHECK_BOX),
            self.is_visible(StatusesLocators.STATUS_ID_COLUMN),
            self.is_visible(StatusesLocators.NAME_COLUMN),
            self.is_visible(StatusesLocators.SLUG_COLUMN)
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

    def delete_status_name(self):
        self.delete_text(StatusesLocators.STATUS_NAME_INPUT)

    def delete_status_slug(self):
        self.delete_text(StatusesLocators.STATUS_SLUG_INPUT)

    def is_status_exist(self, email):
        try:
            self.find_element(StatusesLocators.get_row_by_status_name(name))
            return True
        except:
            return False 