from selenium.common.exceptions import TimeoutException

from pages.actions.users_actions import UsersActions
from pages.base_page import BasePage
from pages.locators.users_locators import UsersLocators


class UsersPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = UsersActions(driver, base_url)

    def enter_user_email(self, email):
        self.actions.change_user_email(email)

    def input_user_data(self, email, first_name, last_name):
        self.enter_user_email(email)
        self.actions.enter_user_first_name(first_name)
        self.actions.enter_user_last_name(last_name)
        self.save_entity()

    def get_user_data_by_email(self, email):
        return self.actions.find_user_data_by_email_column(email)

    def get_all_users_data(self):
        return self.actions.find_all_users_data()

    def delete_user_first_name(self):
        self.actions.delete_user_first_name()

    def delete_user_last_name(self):
        self.actions.delete_user_last_name()

    def delete_user_email(self):
        self.actions.delete_user_email()

    def users_table_is_loaded(self):
        columns_visible = all([
            self.is_presence(UsersLocators.HEADER_CHECK_BOX),
            self.is_clickable(UsersLocators.CREATE_USER_BUTTON),
            self.is_clickable(UsersLocators.ID_COLUMN),
            self.is_clickable(UsersLocators.EMAIL_COLUMN),
            self.is_clickable(UsersLocators.FIRST_NAME_COLUMN),
            self.is_clickable(UsersLocators.LAST_NAME_COLUMN),
            self.is_clickable(UsersLocators.CREATED_AT_COLUMN)
        ])
        return columns_visible

    def users_table_is_empty(self):
        empty_table = all([
            self.is_visible(UsersLocators.EMPTY_STATE),
            self.is_visible(UsersLocators.EMPTY_STATE_ICON),
            self.is_visible(UsersLocators.EMPTY_STATE_TITLE),
            self.is_visible(UsersLocators.EMPTY_STATE_TEXT),
            self.is_visible(UsersLocators.CREATE_USER_BUTTON)
        ])
        return empty_table

    def email_validation_error_is_visible(self):
        return self.is_visible(UsersLocators.EMAIL_FORMAT_ERROR)

    def is_user_exist(self, email):
        try:
            self.find_element(UsersLocators.get_row_by_email(email))
            return True
        except TimeoutException:
            return False

    def click_on_row(self, email):
        self.find_element(UsersLocators.get_row_by_email(email)).click()
