from pages.locators.statuses_locators import StatusesLocators
from pages.base_page import BasePage

class StatusesActions(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        
    def start_status_creation(self):
        self.click(StatusesLocators.CREATE_STATUS_BUTTON)

    def enter_status_name(self, name):
         self.enter_text(StatusesLocators.STATUS_NAME_INPUT, name)

    def enter_status_slug(self, slug):
         self.enter_text(StatusesLocators.STATUS_SLUG_INPUT, slug)

    def find_status_data_by_name_colum(self, name):
        row = self.find_element(StatusesLocators.get_row_by_status_name(name))
        slug = row.find_element(*StatusesLocators.SLUG_COLUMN).text
        return slug