from selenium.webdriver.common.by import By

class LabelsLocators:
        LABEL_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')
        
        @staticmethod
        def get_row_by_label_name(name):
                return (By.XPATH, f'//td[contains(@class, "column-name")]//span[text()="{name}"]/ancestor::tr')