from selenium.webdriver.common.by import By

class LabelsLocators:
        LABEL_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
        LABEL_HEADER_CHECK_BOX = (By.CSS_SELECTOR, '.select-all input')
        LABEL_ID_COLUMN = (By.CSS_SELECTOR, '[data-field="id"]')
        LABEL_NAME_COLUMN = (By.CSS_SELECTOR, '[data-field="name"]')
        LAST_NAME_COLUMN = (By.CSS_SELECTOR, '[data-field="lastName"]')
        LABEL_CREATED_AT_COLUMN = (By.CSS_SELECTOR, '[data-field="createdAt"]')
        LABEL_ID_CELL = (By.CSS_SELECTOR, '.column-id span')
        LABEL_NAME_CELL = (By.CSS_SELECTOR, '.column-name span')
        LABEL_CREATED_AT_CELL = (By.CSS_SELECTOR, '.column-createdAt span')
        LABELS_TABLE = (By.CSS_SELECTOR,'.MuiTableBody-root tr')
        LABELS_EMPTY_STATE = (By.CSS_SELECTOR, '.RaEmpty-message')
        LABELS_EMPTY_STATE_ICON  = (By.CSS_SELECTOR, '[data-testid="InboxIcon"]')
        LABELS_EMPTY_STATE_TITLE = (By.XPATH, '//p[text()="No Labels yet."]')
        LABELS_EMPTY_STATE_TEXT = (By.XPATH, '//p[text()="Do you want to add one?"]')
        LABELS_CREATE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Create"]')

        @staticmethod
        def get_row_by_label_name(name):
                return (By.XPATH, f'//td[contains(@class, "column-name")][normalize-space()="{name}"]/ancestor::tr')