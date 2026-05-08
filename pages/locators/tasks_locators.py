from selenium.webdriver.common.by import By

class TasksLocators:
    TITLE_INPUT = (By.CSS_SELECTOR, 'input[name="title"]')
    CONTENT_INPUT = (By.CSS_SELECTOR, 'textarea[name="content"]')
    TASK_ID_VALUE = (By.CSS_SELECTOR, ".ra-field-id > .MuiTypography-root:last-child")
    COLUMN_BY_STATUS = (By.XPATH, '//div[contains(@class, "css-1xphtog")]')
    STATUS_NAME_IN_COLUMN = (By.XPATH, ".//h6")
    TASK_CARD = (By.XPATH, ".//div[contains(@class, 'MuiCard-root')]")
    CARD_TITLE = (By.XPATH, ".//div[contains(@class, 'MuiTypography-h5')]")
    CARD_CONTENT = (By.XPATH, ".//p[contains(@class, 'MuiTypography-body2')]")
    CARD_INDEX = (By.XPATH, ".//p[contains(@class, 'MuiTypography-body1')]")
    EDIT_BUTTON = (By.XPATH, ".//a[@aria-label='Edit']")
    SHOW_BUTTON = (By.XPATH, ".//a[@aria-label='Show']")

    @staticmethod
    def get_combobox_label_by_name(label_name):
        return By.XPATH, f"//label[.//span[text()='{label_name}']]" 
    
    @staticmethod
    def combobox_by_id(element_id):
        return By.ID, element_id
    
    @staticmethod
    def listbox_by_id(element_id):
        return By.ID, element_id
    
    @staticmethod    
    def option_by_text(option_text):
        return By.XPATH, f".//li[contains(text(), '{option_text}')]"
    
    @staticmethod
    def get_task_in_status_column(status, task_title):
        return (By.XPATH, f"//h6[text()='{status}']/ancestor::div[@data-rfd-droppable-id='1']//div[text()='{task_title}']")
    
    @staticmethod   
    def get_status_column_by_name(column_name):
        return (By.XPATH, f"//h6[text()='{column_name}']")