from pages.locators.users_locators import UsersLocators
from pages.base_page import BasePage

class UsersActions(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
    
    def start_user_creation(self):
        self.click(UsersLocators.CREATE_USER_BUTTON)

    def enter_user_email(self, email):
         self.enter_text(UsersLocators.EMAIL_INPUT, email)

    def enter_user_first_name(self, first_name):
         self.enter_text(UsersLocators.FIRST_NAME_INPUT, first_name)

    def enter_user_last_name(self, last_name):
         self.enter_text(UsersLocators.LAST_NAME_INPUT, last_name)

    def save_user(self):
        self.click(UsersLocators.SAVE_USER_BUTTON)

    def find_user_data_by_email_colum(self, email):
        row = self.find_element(UsersLocators.get_row_by_email(email))
        first_name = row.find_element(*UsersLocators.FIRST_NAME_CELL).text
        last_name = row.find_element(*UsersLocators.LAST_NAME_CELL).text
        return first_name, last_name