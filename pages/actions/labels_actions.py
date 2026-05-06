from pages.locators.labels_locators import LabelsLocators
from pages.base_page import BasePage

class LabelsActions(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def enter_label_name(self, name):
         self.enter_text(LabelsLocators.LABEL_NAME_INPUT, name)
