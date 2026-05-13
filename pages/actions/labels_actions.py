from pages.locators.labels_locators import LabelsLocators
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class LabelsActions(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)


    def enter_label_name(self, name):
        self.delete_text(LabelsLocators.LABEL_NAME_INPUT)
        self.enter_text(LabelsLocators.LABEL_NAME_INPUT, name)


    def find_label_data_by_name(self, name):
        row = self.find_element(LabelsLocators.get_row_by_label_name(name))
        try:
            created_at = row.find_element(*LabelsLocators.LABEL_CREATED_AT_CELL).text
            created_at = 'Дата задана'
        except NoSuchElementException:
            created_at = "Не задана"
        return {
                "id": self.find_in_element(row, LabelsLocators.LABEL_ID_CELL).text,
                "name": self.find_in_element(row, LabelsLocators.LABEL_NAME_CELL).text,
                "createdAt": created_at
                }


    def find_all_labels_data(self):
        rows = self.find_elements(LabelsLocators.LABELS_TABLE)
        result = []
        for row in rows:
            try:
                created_at = row.find_element(*LabelsLocators.LABEL_CREATED_AT_CELL).text
            except NoSuchElementException:
                created_at = "Не задана"
            row_data = {
                "id": self.find_in_element(row, LabelsLocators.LABEL_ID_CELL).text,
                "name": self.find_in_element(row, LabelsLocators.LABEL_NAME_CELL).text,
                "createdAt": created_at
                }
            result.append(row_data)
        return result