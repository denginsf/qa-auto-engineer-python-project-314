from selenium.webdriver.common.by import By


class UsersLocators:
    #Форма юзеров
    FORM = (By.CSS_SELECTOR, '.MuiStack-root')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="lastName"]')
    SAVE_USER_BUTTON = (By.XPATH, '//button[@type="submit" and contains(text(), "Save")]')
    SNACKBAR = (By.XPATH, '//div[text()="Element created"]')
    ERROR_SNACKBAR = (By.XPATH, '//div[text()="The form is not valid. Please check for errors"]')
    UPDATED_SNACKBAR = (By.XPATH, '//div[text()="Element updated"]')

    #Страница юзеров
    EMAIL_CELL = (By.CSS_SELECTOR, '.column-email span')
    FIRST_NAME_CELL = (By.CSS_SELECTOR, '.column-firstName span')
    LAST_NAME_CELL = (By.CSS_SELECTOR, '.column-lastName span')
    CREATE_USER_BUTTON = (By.CSS_SELECTOR, '[aria-label="Create"]')
    HEADER_CHECK_BOX = (By.CSS_SELECTOR, '.select-all input')
    ID_COLUMN = (By.CSS_SELECTOR, '[data-field="id"]')
    EMAIL_COLUMN = (By.CSS_SELECTOR, '[data-field="email"]')
    FIRST_NAME_COLUMN = (By.CSS_SELECTOR, '[data-field="firstName"]')
    LAST_NAME_COLUMN = (By.CSS_SELECTOR, '[data-field="lastName"]')
    CREATED_AT_COLUMN = (By.CSS_SELECTOR, '[data-field="createdAt"]')
    REQUIRED_ERROR = (By.XPATH, '//p[text()="Required"]')
    EMAIL_FORMAT_ERROR = (By.XPATH, '//p[text()="Incorrect email format"]')
    
    @staticmethod
    def get_row_by_email(email):
        return (By.XPATH, f'//span[text()="{email}"]/ancestor::tr')