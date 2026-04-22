from pages.actions.users_actions import UsersActions
from pages.locators.users_locators import UsersLocators
from pages.base_page import BasePage


class UsersPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = UsersActions(driver, base_url)
    
    def enter_user_email(self, email):
        self.enter_text(UsersLocators.EMAIL_INPUT, email)

    def save_user(self):
        self.click(UsersLocators.SAVE_USER_BUTTON)

    def input_user_data(self, email, first_name, last_name):
        self.enter_user_email(email)
        self.actions.enter_user_first_name(first_name)
        self.actions.enter_user_last_name(last_name)
        self.save_user()

    def find_succes_snackbar(self):
        return self.is_visible(UsersLocators.SNACKBAR)

    def find_error_snackbar(self):
        return self.is_visible(UsersLocators.ERROR_SNACKBAR)

    def find_error_snackbar(self):
        return self.is_visible(UsersLocators.ERROR_SNACKBAR)

    def find_user_updated_snackbar(self):
        return self.is_visible(UsersLocators.UPDATED_SNACKBAR)    

    def open_user_creation_form(self):
        self.actions.start_user_creation()
        return self.is_visible(UsersLocators.FORM)

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
            self.is_visible(UsersLocators.CREATED_AT_COLUMN),
        ]
        )
        return columns_visible

    def get_required_errors_count(self):        
        return len(self.driver.find_elements(*UsersLocators.REQUIRED_ERROR))

    def email_validation_error_is_visible(self):
         return self.is_visible(UsersLocators.EMAIL_FORMAT_ERROR)

    def click_on_row(self, email):
        self.find_element(UsersLocators.get_row_by_email(email)).click()
