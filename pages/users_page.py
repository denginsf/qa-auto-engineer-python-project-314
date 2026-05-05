from pages.actions.users_actions import UsersActions
from pages.locators.users_locators import UsersLocators
from pages.base_page import BasePage


class UsersPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = UsersActions(driver, base_url)
    
    def enter_user_email(self, email):
        self.enter_text(UsersLocators.EMAIL_INPUT, email)

    def input_user_data(self, email, first_name, last_name):
        self.enter_user_email(email)
        self.actions.enter_user_first_name(first_name)
        self.actions.enter_user_last_name(last_name)
        self.save_entity()

    def get_user_data_by_email(self, email):
        return self.actions.find_user_data_by_email_colum(email)

    def delete_user_first_name(self):
        self.delete_text(UsersLocators.FIRST_NAME_INPUT)

    def delete_user_last_name(self):
        self.delete_text(UsersLocators.LAST_NAME_INPUT)

    def delete_user_email(self):
        self.delete_text(UsersLocators.EMAIL_INPUT)
    
    def users_table_is_loaded(self):
        columns_visible = all([
            self.is_presence(UsersLocators.HEADER_CHECK_BOX),
            self.is_visible(UsersLocators.ID_COLUMN),
            self.is_visible(UsersLocators.EMAIL_COLUMN),
            self.is_visible(UsersLocators.FIRST_NAME_COLUMN),
            self.is_visible(UsersLocators.LAST_NAME_COLUMN),
            self.is_visible(UsersLocators.CREATED_AT_COLUMN)
        ]
        )
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

    def select_all_users(self):
        self.find_element(UsersLocators.SELECT_ALL).click()

    def get_required_errors_count(self):        
        return len(self.driver.find_elements(*UsersLocators.REQUIRED_ERROR))

    def email_validation_error_is_visible(self):
         return self.is_visible(UsersLocators.EMAIL_FORMAT_ERROR)

    def is_user_exist(self, email):
        try:
            self.find_element(UsersLocators.get_row_by_email(email))
            return True
        except:
            return False 

    def click_on_row(self, email):
        self.find_element(UsersLocators.get_row_by_email(email)).click()
