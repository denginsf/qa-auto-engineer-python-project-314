from pages.actions.labels_actions import LabelsActions
from pages.locators.labels_locators import LabelsLocators
from pages.base_page import BasePage

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
        except:
            return False
        
    def labels_table_is_loaded(self):
        columns_visible = all([
            self.is_presence(LabelsLocators.LABEL_HEADER_CHECK_BOX),
            self.is_visible(LabelsLocators.LABEL_ID_COLUMN),
            self.is_visible(LabelsLocators.LABEL_NAME_COLUMN),
            self.is_visible(LabelsLocators.LABEL_CREATED_AT_COLUMN)
        ]
        )
        return columns_visible

    def get_all_labels_data(self):
        rows = self.find_elements(LabelsLocators.LABELS_TABLE)
        result = []
        for row in rows:
            row_data = {
                "id": self.find_in_element(row, LabelsLocators.LABEL_ID_CELL).text,
                "name": self.find_in_element(row, LabelsLocators.LABEL_NAME_CELL).text,
                "createdAt": self.find_in_element(row, LabelsLocators.LABEL_CREATED_AT_CELL).text
                }
            result.append(row_data)
        return result
    
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