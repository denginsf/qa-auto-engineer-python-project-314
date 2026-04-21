from selenium.webdriver.common.by import By


class UsersLocators:
    #Форма юзеров
    FORM = (By.CSS_SELECTOR, '.MuiStack-root')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="lastName"]')
    SAVE_USER_BUTTON = (By.XPATH, '//button[@type="submit" and contains(text(), "Save")]')
    SNACKBAR = (By.XPATH, '//div[text()="Element created"]')

    #Страница юзеров
    EMAIL_CELL = (By.CSS_SELECTOR, '.column-email span')
    FIRST_NAME_CELL = (By.CSS_SELECTOR, '.column-firstName span')
    LAST_NAME_CELL = (By.CSS_SELECTOR, '.column-lastName span')
    CREATE_USER_BUTTON = (By.CSS_SELECTOR, '[aria-label="Create"]')
    
    
    @staticmethod
    def get_row_by_email(email):
        return (By.XPATH, f'//span[text()="{email}"]/ancestor::tr')