from selenium.common.exceptions import TimeoutException

from pages.actions.tasks_actions import TasksActions
from pages.base_page import BasePage
from pages.locators.tasks_locators import TasksLocators


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

    def change_assignee(self, assignee):
        self.actions.select_assignee(assignee)
    
    def add_label(self, label):
        self.actions.select_label(label)

    def change_status(self, status):
        self.actions.select_status(status)

    def change_content(self, content):
        self.actions.change_content(content)

    def change_title(self, title):
        self.actions.change_title(title)

    def get_task_id_value(self):
        return self.find_element(TasksLocators.TASK_ID_VALUE).text
    
    def is_task_present_in_status(self, status, task_title):
        try:
            self.find_element(TasksLocators.get_task_in_status_column(status, task_title))
            return True
        except TimeoutException:
            return False

    def task_page_is_loaded(self):
        columns_visible = all([
            self.actions.get_combobox_by_label('Assignee'),
            self.actions.get_combobox_by_label('Status'),
            self.actions.get_combobox_by_label('Label'),
            self.actions.are_all_columns_present()
        ]
        )
        return columns_visible
    
    def get_task_data_by_name(self, name):
        return self.actions.find_tasks_data_by_name(name)

    def get_all_tasks_data(self):
        return self.actions.find_all_tasks_data()
    
    def filter_by_assignee(self, assignee):
        count_before = len(self.find_elements(TasksLocators.TASK_CARD))
        self.actions.select_assignee(assignee)
        self.wait_for_count_stable(TasksLocators.TASK_CARD, count_before)

    def filter_by_status(self, status):
        count_before = len(self.find_elements(TasksLocators.TASK_CARD))
        self.actions.select_status(status)
        self.wait_for_count_stable(TasksLocators.TASK_CARD, count_before)

    def filter_by_label(self, label):
        count_before = len(self.find_elements(TasksLocators.TASK_CARD))
        self.actions.select_label(label)
        self.wait_for_count_stable(TasksLocators.TASK_CARD, count_before)

    def start_task_edit_by_name(self, task_name):
        task_card = self.find_element(TasksLocators.get_task_card_by_name(task_name))
        self.find_in_element(task_card, TasksLocators.EDIT_BUTTON).click()

    def open_show_task(self, task_name):
        self.actions.click_show_task(task_name)