from selenium.webdriver.common.by import By


class UsersLocators:
    #Форма юзеров
    FORM = (By.CSS_SELECTOR, '.MuiStack-root')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="lastName"]')
    SNACKBAR = (By.XPATH, '//div[text()="Element created"]')
    ERROR_SNACKBAR = (By.XPATH, '//div[text()="The form is not valid. Please check for errors"]')
    UPDATED_SNACKBAR = (By.XPATH, '//div[text()="Element updated"]')
    DELETED_SNACKBAR = (By.XPATH, '//div[text()="Element deleted"]')
    ALL_DELETED_SNACKBAR = (By.XPATH, '//div[contains(text(), "elements deleted")]')

    #Страница юзеров
    USERS_TABLE_ROWS = (By.CSS_SELECTOR,'.MuiTableBody-root tr')
    EMAIL_CELL = (By.CSS_SELECTOR, '.column-email span')
    USER_ID_CELL = (By.CSS_SELECTOR, '.column-id span')
    FIRST_NAME_CELL = (By.CSS_SELECTOR, '.column-firstName span')
    LAST_NAME_CELL = (By.CSS_SELECTOR, '.column-lastName span')
    CREATED_AT_CELL = (By.CSS_SELECTOR, '.column-createdAt span')
    CREATE_USER_BUTTON = (By.CSS_SELECTOR, '[aria-label="Create"]')
    DELETE_USER_BUTTON = (By.CSS_SELECTOR, '[aria-label="Delete"]')
    HEADER_CHECK_BOX = (By.CSS_SELECTOR, '.select-all input')
    SELECT_ALL = (By.CSS_SELECTOR, '.select-all')
    ID_COLUMN = (By.CSS_SELECTOR, '[data-field="id"]')
    EMAIL_COLUMN = (By.CSS_SELECTOR, '[data-field="email"]')
    FIRST_NAME_COLUMN = (By.CSS_SELECTOR, '[data-field="firstName"]')
    LAST_NAME_COLUMN = (By.CSS_SELECTOR, '[data-field="lastName"]')
    CREATED_AT_COLUMN = (By.CSS_SELECTOR, '[data-field="createdAt"]')
    REQUIRED_ERROR = (By.XPATH, '//p[text()="Required"]')
    EMAIL_FORMAT_ERROR = (By.XPATH, '//p[text()="Incorrect email format"]')
    EMPTY_STATE = (By.CSS_SELECTOR, '.RaEmpty-message')
    EMPTY_STATE_ICON = (By.CSS_SELECTOR, '[data-testid="InboxIcon"]')
    EMPTY_STATE_TITLE = (By.XPATH, '//p[text()="No Users yet."]')
    EMPTY_STATE_TEXT = (By.XPATH, '//p[text()="Do you want to add one?"]')

    @staticmethod
    def get_row_by_email(email):
        return (By.XPATH, f'//span[text()="{email}"]/ancestor::tr')