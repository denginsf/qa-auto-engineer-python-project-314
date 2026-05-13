from selenium.webdriver.common.by import By

class StatusesLocators:
    STATUSES_TABLE_ROWS = (By.CSS_SELECTOR,'.MuiTableBody-root tr')
    STATUS_ID_CELL = (By.CSS_SELECTOR, '.column-id span')
    SLUG_CELL = (By.CSS_SELECTOR, '.column-slug span')
    SLUG_COLUMN = (By.CSS_SELECTOR, '[data-field="slug"]')
    CREATED_AT_COLUMN = (By.CSS_SELECTOR, '[data-field="createdAt"]')
    STATUS_NAME_CELL = (By.CSS_SELECTOR, '.column-name span')
    CREATED_AT_CELL = (By.CSS_SELECTOR, '.column-createdAt span')
    STATUS_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
    STATUS_SLUG_INPUT = (By.CSS_SELECTOR, 'input[name="slug"]')
    STATUS_HEADER_CHECK_BOX = (By.CSS_SELECTOR, '.select-all input')
    STATUS_ID_COLUMN = (By.CSS_SELECTOR, '[data-field="id"]')
    NAME_COLUMN = (By.CSS_SELECTOR, '[data-field="name"]')
    STATUSES_EMPTY_STATE = (By.CSS_SELECTOR, '.RaEmpty-message')
    STATUSES_EMPTY_STATE_ICON = (By.CSS_SELECTOR, '[data-testid="InboxIcon"]')
    STATUSES_EMPTY_STATE_TITLE = (By.XPATH, '//p[text()="No Task statuses yet."]')
    STATUSES_EMPTY_STATE_TEXT = (By.XPATH, '//p[text()="Do you want to add one?"]')
    CREATE_STATUS_BUTTON = (By.CSS_SELECTOR, '[aria-label="Create"]')

    @staticmethod
    def get_row_by_status_name(name):
        return (By.XPATH, f'//td[contains(@class, "column-name")]//span[text()="{name}"]/ancestor::tr')