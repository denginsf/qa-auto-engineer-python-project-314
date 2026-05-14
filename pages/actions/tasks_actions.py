from pages.locators.tasks_locators import TasksLocators
from pages.base_page import BasePage


class TasksActions(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)


    def enter_task_title(self, title):
         self.enter_text(TasksLocators.TITLE_INPUT, title)


    def enter_task_content(self, content):
         self.enter_text(TasksLocators.CONTENT_INPUT, content)


    def change_content(self, content):
        self.delete_text(TasksLocators.CONTENT_INPUT)
        self.enter_task_content(content)


    def change_title(self, title):
        self.delete_text(TasksLocators.TITLE_INPUT)
        self.enter_task_title(title)


    def get_combobox_by_label(self, label_name):
        label = self.find_element(TasksLocators.get_combobox_label_by_name(label_name))
        combobox_id = label.get_attribute("for")
        combobox = self.find_element(TasksLocators.combobox_by_id(combobox_id))
        return combobox


    def select_assignee(self, assignee):
        self.get_combobox_by_label('Assignee').click()
        self.click(TasksLocators.option_by_text(assignee))
        self.esc()


    def select_status(self, status):
        self.get_combobox_by_label('Status').click()
        self.click(TasksLocators.option_by_text(status))
        self.esc()


    def select_label(self, label_value):
        self.get_combobox_by_label('Label').click()
        self.click(TasksLocators.option_by_text(label_value))
        self.esc()


    def are_all_columns_present(self):
        expected_columns = ['Draft', 'To Review', 'To Be Fixed', 'To Publish', 'Published']
        for column in expected_columns:
            if not self.is_clickable(TasksLocators.get_status_column_by_name(column)):
                return False
        return True


    def find_tasks_data_by_name(self, task_name):
        task = self.find_element(TasksLocators.get_task_card_by_name(task_name))
        return {
                    "Title": self.find_in_element(task, TasksLocators.CARD_TITLE).text,
                    "Content": self.find_in_element(task, TasksLocators.CARD_CONTENT).text,
                    # "Index": self.find_in_element(task, TasksLocators.CARD_INDEX).text.replace("Index: ", ""),
                    "Edit_button_present": self.is_clickable_in_element(task, TasksLocators.EDIT_BUTTON),
                    "Show_button_present": self.is_clickable_in_element(task, TasksLocators.SHOW_BUTTON)
                }


    def find_all_tasks_data(self):
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
                    "Edit_button_present": self.is_clickable_in_element(card, TasksLocators.EDIT_BUTTON),
                    "Show_button_present": self.is_clickable_in_element(card, TasksLocators.SHOW_BUTTON)
                }
                tasks_list.append(card_data)
            result[status_name] = tasks_list
        return result
