from pages.actions.tasks_actions import TasksActions
from pages.locators.tasks_locators import TasksLocators
from pages.base_page import BasePage


class TasksPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.actions = TasksActions(driver, base_url)

    def create_task(self, assignee, title, content, status, label):
        self.actions.select_assignee(assignee)
        self.actions.enter_task_title(title)
        self.actions.enter_task_content(content)
        self.actions.select_status(status)
        self.actions.select_label(label)
        self.save_entity()

    def get_task_id_value(self):
        return self.find_element(TasksLocators.TASK_ID_VALUE).text
    
    def is_task_present_in_satus(self, status, task_title):
        try:
            self.is_visible(TasksLocators.get_task_in_status_column(status, task_title))
            return True
        except:
            return False

    def task_table_is_loaded(self):
        columns_visible = all([
            self.actions.get_combobox_by_label('Assignee'),
            self.actions.get_combobox_by_label('Status'),
            self.actions.get_combobox_by_label('Label'),
            self.actions.are_all_columns_present()
        ]
        )
        return columns_visible
    
    def get_all_statuses_data(self):
        statuses = self.find_elements(TasksLocators.COLUMN_BY_STATUS)
        result = {}
        for status in statuses:
            status_name = status.find_element(*TasksLocators.STATUS_NAME_IN_COLUMN).text
            task_cards = status.find_elements(*TasksLocators.TASK_CARD)
            tasks_list = []
            for card in task_cards:
                card_data = {
                    "Title": self.find_in_element(card, TasksLocators.CARD_TITLE).text,
                    "Content": self.find_in_element(card, TasksLocators.CARD_CONTENT).text,
                    "Index": self.find_in_element(card, TasksLocators.CARD_INDEX).text.replace("Index: ", ""),
                    "Edit_button_present": self.is_visible(TasksLocators.EDIT_BUTTON),
                    "Show_button_present": self.is_visible(TasksLocators.SHOW_BUTTON)
                }
                tasks_list.append(card_data)
            result[status_name] = tasks_list
        return result
    
    def filter_by_assignee(self, assignee):
        count_cards_before = len(self.find_elements(TasksLocators.TASK_CARD))
        self.actions.select_assignee(assignee)
        self.wait.until(lambda d: len(d.find_elements(*TasksLocators.TASK_CARD)) != count_cards_before)

    def filter_by_status(self, status):
        count_cards_before = len(self.find_elements(TasksLocators.TASK_CARD))
        self.actions.select_status(status)
        self.wait.until(lambda d: len(d.find_elements(*TasksLocators.TASK_CARD)) != count_cards_before)

    def filter_by_label(self, label):
        count_cards_before = len(self.find_elements(TasksLocators.TASK_CARD))
        self.actions.select_label(label)
        self.wait.until(lambda d: len(d.find_elements(*TasksLocators.TASK_CARD)) != count_cards_before)