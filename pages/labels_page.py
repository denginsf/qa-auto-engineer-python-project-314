from selenium.common.exceptions import TimeoutException

from pages.actions.labels_actions import LabelsActions
from pages.base_page import BasePage
from pages.locators.labels_locators import LabelsLocators


class LabelsPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = LabelsActions(driver, base_url)

    def input_label_data(self, name):
        self.actions.enter_label_name(name)
        self.save_entity()

    def is_label_exist(self, name):
        try:
            self.find_element(LabelsLocators.get_row_by_label_name(name))
            return True
        except TimeoutException:
            return False
        
    def labels_table_is_loaded(self):
        columns_visible = all([
            self.is_presence(LabelsLocators.LABEL_HEADER_CHECK_BOX),
            self.is_clickable(LabelsLocators.LABEL_ID_COLUMN),
            self.is_clickable(LabelsLocators.LABEL_NAME_COLUMN),
            self.is_clickable(LabelsLocators.LABEL_CREATED_AT_COLUMN)
        ]
        )
        return columns_visible

    def get_label_data_by_name(self, name):
        return self.actions.find_label_data_by_name(name)

    def get_all_labels_data(self):
        return self.actions.find_all_labels_data()
    
    def click_on_label_row(self, name):
        self.find_element(LabelsLocators.get_row_by_label_name(name)).click()

    def delete_label_name(self):
        self.delete_text(LabelsLocators.LABEL_NAME_INPUT)

    def labels_table_is_empty(self):
        empty_table = all([
            self.is_visible(LabelsLocators.LABELS_EMPTY_STATE),
            self.is_visible(LabelsLocators.LABELS_EMPTY_STATE_ICON),
            self.is_visible(LabelsLocators.LABELS_EMPTY_STATE_TITLE),
            self.is_visible(LabelsLocators.LABELS_EMPTY_STATE_TEXT),
            self.is_visible(LabelsLocators.LABELS_CREATE_BUTTON)
        ])
        return empty_table