from pages.actions.labels_actions import LabelsActions
from pages.locators.labels_locators import LabelsLocators
from pages.base_page import BasePage

class LabelsPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = LabelsActions(driver, base_url)

    def input_status_data(self, name):
        self.actions.enter_label_name(name)
        self.save_entity()

    def is_label_exist(self, name):
        if self.find_element(LabelsLocators.get_row_by_label_name(name)):
            return True
        else:
            return False