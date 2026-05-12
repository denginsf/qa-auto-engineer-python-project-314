from pages.locators.statuses_locators import StatusesLocators
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class StatusesActions(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)


    def enter_status_name(self, name):
         self.enter_text(StatusesLocators.STATUS_NAME_INPUT, name)


    def enter_status_slug(self, slug):
         self.enter_text(StatusesLocators.STATUS_SLUG_INPUT, slug)


    def delete_status_name(self):
        self.delete_text(StatusesLocators.STATUS_NAME_INPUT)


    def delete_status_slug(self):
        self.delete_text(StatusesLocators.STATUS_SLUG_INPUT)


    def find_status_data_by_name_column(self, name):
        row = self.find_element(StatusesLocators.get_row_by_status_name(name))
        try:
            created_at = row.find_element(*StatusesLocators.CREATED_AT_CELL).text
            created_at = 'Дата задана'
        except NoSuchElementException:
            created_at = "Не задана"
        return {
                "id": row.find_element(*StatusesLocators.STATUS_ID_CELL).text,
                "slug": row.find_element(*StatusesLocators.SLUG_CELL).text,
                "createdAt": created_at
                }

    
    def find_all_status_data(self):
        rows = self.find_elements(StatusesLocators.STATUSES_TABLE_ROWS)
        result = []
        for row in rows:
            try:
                created_at = row.find_element(*StatusesLocators.CREATED_AT_CELL).text
            except NoSuchElementException:
                created_at = "Не задана"
            raw_data = {
                    "id": row.find_element(*StatusesLocators.STATUS_ID_CELL).text,
                    "name": row.find_element(*StatusesLocators.STATUS_NAME_CELL).text,    
                    "slug": row.find_element(*StatusesLocators.SLUG_CELL).text,
                    "createdAt": created_at
                    }
            result.append(raw_data)
        return result