from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.locators.users_locators import UsersLocators


class UsersActions(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def enter_user_first_name(self, first_name):
        self.enter_text(UsersLocators.FIRST_NAME_INPUT, first_name)

    def enter_user_last_name(self, last_name):
        self.enter_text(UsersLocators.LAST_NAME_INPUT, last_name)

    def change_user_email(self, email):
        self.delete_text(UsersLocators.EMAIL_INPUT)
        self.enter_text(UsersLocators.EMAIL_INPUT, email)

    def delete_user_first_name(self):
        self.delete_text(UsersLocators.FIRST_NAME_INPUT)

    def delete_user_last_name(self):
        self.delete_text(UsersLocators.LAST_NAME_INPUT)

    def delete_user_email(self):
        self.delete_text(UsersLocators.EMAIL_INPUT)   

    def find_user_data_by_email_column(self, email):
        row = self.find_element(UsersLocators.get_row_by_email(email))
        # try:
        # created_at = row.find_element(*UsersLocators.CREATED_AT_CELL).text
        # created_at = 'Дата задана'
        # except NoSuchElementException:
        # created_at = "Не задана"
        return {
                "id": row.find_element(*UsersLocators.USER_ID_CELL).text,
                "first_name": row.find_element(*UsersLocators.FIRST_NAME_CELL).text,
                "last_name": row.find_element(*UsersLocators.LAST_NAME_CELL).text
        # "createdAt": created_at
                }

    def find_all_users_data(self):
        rows = self.find_elements(UsersLocators.USERS_TABLE_ROWS)
        result = []
        for row in rows:
            try:
                created_at = row.find_element(*UsersLocators.CREATED_AT_CELL).text
            except NoSuchElementException:
                created_at = "Не задана"
            raw_data = {
                    "id": row.find_element(*UsersLocators.USER_ID_CELL).text,
                    "first_name": row.find_element(*UsersLocators.FIRST_NAME_CELL).text,
                    "last_name": row.find_element(*UsersLocators.LAST_NAME_CELL).text,
                    "createdAt": created_at
                    }
            result.append(raw_data)
        return result