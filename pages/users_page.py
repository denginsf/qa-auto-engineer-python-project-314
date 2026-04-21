from pages.actions.users_actions import UsersActions
from pages.locators.users_locators import UsersLocators
from pages.base_page import BasePage


class UsersPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = UsersActions(driver, base_url)

    def create_user(self, email, first_name, last_name):
        self.actions.enter_user_email(email)
        self.actions.enter_user_first_name(first_name)
        self.actions.enter_user_last_name(last_name)
        self.actions.save_user()

    def find_succes_snackbar(self):
        return self.is_visible(UsersLocators.SNACKBAR)

    def open_user_creation_form(self):
        self.actions.start_user_creation()
        return self.is_visible(UsersLocators.FORM)

    def get_user_data_by_email(self, email):
        return self.actions.find_user_data_by_email_colum(email)