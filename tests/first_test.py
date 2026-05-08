from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.users_page import UsersPage
from pages.statuses_page import StatusesPage
from pages.labels_page import LabelsPage
from pages.tasks_page import TasksPage


def test_login(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'


def test_logout(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.logout()
    login_page = LoginPage(driver, base_url)
    assert login_page.find_lock_icon() == True


def test_smoke_users_list(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    assert users_page.users_table_is_loaded()
    first_name, last_name = users_page.get_user_data_by_email('john@google.com')
    assert first_name == 'John'
    assert last_name == 'Doe'


def test_create_user(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.open_entity_creation_form() == True
    users_page.input_user_data('test@test.com', 'Alex', 'Test')
    assert users_page.find_succes_snackbar() == True
    main_page.go_to_users()
    first_name, last_name = users_page.get_user_data_by_email('test@test.com')
    assert first_name == 'Alex'
    assert last_name == 'Test'


def test_user_update(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.click_on_row('john@google.com')
    users_page.delete_user_email()
    users_page.delete_user_first_name()
    users_page.delete_user_last_name()
    users_page.save_entity()
    assert users_page.find_error_snackbar()
    assert users_page.get_required_errors_count() == 3
    users_page.input_user_data('test', 'Ivan', 'Doe')
    assert users_page.email_validation_error_is_visible() == True
    users_page.delete_user_email()
    users_page.enter_user_email('john_changed@google.com')
    users_page.save_entity()
    first_name, last_name = users_page.get_user_data_by_email('john_changed@google.com')
    assert first_name == 'Ivan'
    assert last_name == 'Doe'
    assert users_page.find_updated_snackbar()


def test_user_delete(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.click_on_row('john@google.com')
    users_page.delete_entity()
    assert users_page.find_deleted_snackbar()
    assert users_page.is_user_exist('john@google.com') == False


def test_all_users_delete(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.select_all_users()
    users_page.delete_entity()
    assert users_page.find_all_entitys_deleted_snackbar()
    assert users_page.users_table_is_empty() == True


def test_create_status(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    statuses_page.open_entity_creation_form() == True
    statuses_page.input_status_data('test_status', 'test')
    assert statuses_page.find_succes_snackbar() == True
    main_page.go_to_statuses()
    slug = statuses_page.get_status_data_by_name('test_status')
    assert slug == 'test'

def test_smoke_statuses_list(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    assert statuses_page.statuses_table_is_loaded()
    slug = statuses_page.get_status_data_by_name('Draft')
    assert slug == 'draft'

def test_status_update(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    statuses_page.click_on_status_row('Draft')
    statuses_page.delete_status_name()
    statuses_page.delete_status_slug()
    statuses_page.save_entity()
    assert statuses_page.find_error_snackbar()
    assert statuses_page.get_required_errors_count() == 2
    statuses_page.input_status_data('test_updated', 'updated')
    slug = statuses_page.get_status_data_by_name('test_updated')
    assert statuses_page.find_updated_snackbar()
    assert slug == 'updated'

def test_status_delete(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    statuses_page.click_on_status_row('Draft')
    statuses_page.delete_entity()
    assert statuses_page.find_deleted_snackbar()
    assert statuses_page.is_status_exist('Draft') == False

def test_all_statuses_delete(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    statuses_page.select_all_entitys()
    statuses_page.delete_entity()
    assert statuses_page.find_all_entitys_deleted_snackbar()
    assert statuses_page.statuses_table_is_empty() == True

def test_create_label(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_labels()
    labels_page = LabelsPage(driver, base_url)
    labels_page.open_entity_creation_form() == True
    labels_page.input_label_data('test_label')
    assert labels_page.find_succes_snackbar() == True
    main_page.go_to_labels()
    assert labels_page.is_label_exist('test_label') == True

def test_smoke_labels_list(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_labels()
    labels_page = LabelsPage(driver, base_url)
    assert labels_page.labels_table_is_loaded()
    labels_list = labels_page.get_all_labels_data()
    assert labels_list == [
    {"id": "1", "name": "bug", "createdAt": "21.12.2023, 03:00:00"},
    {"id": "2", "name": "feature", "createdAt": "21.12.2023, 03:00:00"},
    {"id": "3", "name": "enhancement", "createdAt": "22.12.2023, 03:00:00"},
    {"id": "4", "name": "task", "createdAt": "23.12.2023, 03:00:00"},
    {"id": "5", "name": "critical", "createdAt": "24.12.2023, 03:00:00"}
    ]

def test_update_label(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_labels()
    labels_page = LabelsPage(driver, base_url)
    labels_page.click_on_label_row('task')
    labels_page.delete_label_name()
    labels_page.save_entity()
    assert labels_page.find_error_snackbar()
    assert labels_page.get_required_errors_count() == 1
    labels_page.input_label_data('test_label')
    assert labels_page.find_updated_snackbar()
    assert labels_page.is_label_exist('test_label') == True


def test_label_delete(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_labels()
    labels_page = LabelsPage(driver, base_url)
    labels_page.click_on_label_row('feature')
    labels_page.delete_entity()
    assert labels_page.find_deleted_snackbar()
    assert labels_page.is_label_exist('feature') == False

def test_all_labels_delete(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_labels()
    labels_page = LabelsPage(driver, base_url)
    labels_page.select_all_entitys()
    labels_page.delete_entity()
    assert labels_page.find_all_entitys_deleted_snackbar()
    assert labels_page.labels_table_is_empty() == True

def test_create_task(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_tasks()
    tasks_page = TasksPage(driver, base_url)
    assert tasks_page.open_entity_creation_form() == True
    tasks_page.create_task('emily@example.com', 'Test task', 'Test Content', 'Draft', 'critical')
    assert tasks_page.find_succes_snackbar() == True
    assert tasks_page.get_task_id_value() == '16'
    main_page.go_to_tasks()
    assert tasks_page.is_task_present_in_satus('Draft', 'Test task') == True

def test_smoke_tasks_list(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_tasks()
    tasks_page = TasksPage(driver, base_url)
    assert tasks_page.task_table_is_loaded()
    tasks_list = tasks_page.get_all_statuses_data()
    assert tasks_list == {
        'Draft': [{'Title': 'Task 11', 'Content': 'Description of task 11', 'Index': '3220', 'Edit_button_present': True, 'Show_button_present': True}, 
                  {'Title': 'Task 5', 'Content': 'Description of task 5', 'Index': '3224', 'Edit_button_present': True, 'Show_button_present': True}, 
                  {'Title': 'Task 6', 'Content': 'Description of task 6', 'Index': '3245', 'Edit_button_present': True, 'Show_button_present': True}], 
        'To Review': [{'Title': 'Task 2', 'Content': 'Description of task 2', 'Index': '3161', 'Edit_button_present': True, 'Show_button_present': True}, 
                      {'Title': 'Task 12', 'Content': 'Description of task 12', 'Index': '3230', 'Edit_button_present': True, 'Show_button_present': True}, 
                      {'Title': 'Task 7', 'Content': 'Description of task 7', 'Index': '3266', 'Edit_button_present': True, 'Show_button_present': True}], 
        'To Be Fixed': [{'Title': 'Task 1', 'Content': 'Description of task 1', 'Index': '3140', 'Edit_button_present': True, 'Show_button_present': True}, 
                        {'Title': 'Task 13', 'Content': 'Description of task 13', 'Index': '3240', 'Edit_button_present': True, 'Show_button_present': True}, 
                        {'Title': 'Task 8', 'Content': 'Description of task 8', 'Index': '3287', 'Edit_button_present': True, 'Show_button_present': True}], 
        'To Publish': [{'Title': 'Task 3', 'Content': 'Description of task 3', 'Index': '3182', 'Edit_button_present': True, 'Show_button_present': True}, 
                       {'Title': 'Task 14', 'Content': 'Description of task 14', 'Index': '3250', 'Edit_button_present': True, 'Show_button_present': True}, 
                       {'Title': 'Task 9', 'Content': 'Description of task 9', 'Index': '3308', 'Edit_button_present': True, 'Show_button_present': True}], 
        'Published': [{'Title': 'Task 4', 'Content': 'Description of task 4', 'Index': '3203', 'Edit_button_present': True, 'Show_button_present': True}, 
                      {'Title': 'Task 15', 'Content': 'Description of task 15', 'Index': '3260', 'Edit_button_present': True, 'Show_button_present': True}, 
                      {'Title': 'Task 10', 'Content': 'Description of task 10', 'Index': '3329', 'Edit_button_present': True, 'Show_button_present': True}]}

def test_tasks_filtarion_list(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_tasks()
    tasks_page = TasksPage(driver, base_url)
    assert tasks_page.task_table_is_loaded()
    tasks_list = tasks_page.get_all_statuses_data()
    assert tasks_list == {
        'Draft': [{'Title': 'Task 11', 'Content': 'Description of task 11', 'Index': '3220', 'Edit_button_present': True, 'Show_button_present': True}, 
                  {'Title': 'Task 5', 'Content': 'Description of task 5', 'Index': '3224', 'Edit_button_present': True, 'Show_button_present': True}, 
                  {'Title': 'Task 6', 'Content': 'Description of task 6', 'Index': '3245', 'Edit_button_present': True, 'Show_button_present': True}], 
        'To Review': [{'Title': 'Task 2', 'Content': 'Description of task 2', 'Index': '3161', 'Edit_button_present': True, 'Show_button_present': True}, 
                      {'Title': 'Task 12', 'Content': 'Description of task 12', 'Index': '3230', 'Edit_button_present': True, 'Show_button_present': True}, 
                      {'Title': 'Task 7', 'Content': 'Description of task 7', 'Index': '3266', 'Edit_button_present': True, 'Show_button_present': True}], 
        'To Be Fixed': [{'Title': 'Task 1', 'Content': 'Description of task 1', 'Index': '3140', 'Edit_button_present': True, 'Show_button_present': True}, 
                        {'Title': 'Task 13', 'Content': 'Description of task 13', 'Index': '3240', 'Edit_button_present': True, 'Show_button_present': True}, 
                        {'Title': 'Task 8', 'Content': 'Description of task 8', 'Index': '3287', 'Edit_button_present': True, 'Show_button_present': True}], 
        'To Publish': [{'Title': 'Task 3', 'Content': 'Description of task 3', 'Index': '3182', 'Edit_button_present': True, 'Show_button_present': True}, 
                       {'Title': 'Task 14', 'Content': 'Description of task 14', 'Index': '3250', 'Edit_button_present': True, 'Show_button_present': True}, 
                       {'Title': 'Task 9', 'Content': 'Description of task 9', 'Index': '3308', 'Edit_button_present': True, 'Show_button_present': True}], 
        'Published': [{'Title': 'Task 4', 'Content': 'Description of task 4', 'Index': '3203', 'Edit_button_present': True, 'Show_button_present': True}, 
                      {'Title': 'Task 15', 'Content': 'Description of task 15', 'Index': '3260', 'Edit_button_present': True, 'Show_button_present': True}, 
                      {'Title': 'Task 10', 'Content': 'Description of task 10', 'Index': '3329', 'Edit_button_present': True, 'Show_button_present': True}]}
    tasks_page.filter_by_assignee('jack@yahoo.com')
    filtered_tasks_list = tasks_page.get_all_statuses_data()
    assert filtered_tasks_list == {
        'Draft': [], 
        'To Review': [{'Title': 'Task 12', 'Content': 'Description of task 12', 'Index': '3230', 'Edit_button_present': True, 'Show_button_present': True}], 
        'To Be Fixed': [{'Title': 'Task 13', 'Content': 'Description of task 13', 'Index': '3240', 'Edit_button_present': True, 'Show_button_present': True}], 
        'To Publish': [{'Title': 'Task 3', 'Content': 'Description of task 3', 'Index': '3182', 'Edit_button_present': True, 'Show_button_present': True}, 
                       {'Title': 'Task 14', 'Content': 'Description of task 14', 'Index': '3250', 'Edit_button_present': True, 'Show_button_present': True}], 
        'Published': [{'Title': 'Task 4', 'Content': 'Description of task 4', 'Index': '3203', 'Edit_button_present': True, 'Show_button_present': True}]
        }
    tasks_page.filter_by_status('To Publish')
    filtered_tasks_list = tasks_page.get_all_statuses_data()
    assert filtered_tasks_list == {
        'Draft': [], 
        'To Review': [], 
        'To Be Fixed': [], 
        'To Publish': [{'Title': 'Task 3', 'Content': 'Description of task 3', 'Index': '3182', 'Edit_button_present': True, 'Show_button_present': True}, 
                    {'Title': 'Task 14', 'Content': 'Description of task 14', 'Index': '3250', 'Edit_button_present': True, 'Show_button_present': True}], 
        'Published': []
        }
    tasks_page.filter_by_label('bug')
    filtered_tasks_list = tasks_page.get_all_statuses_data()
    assert filtered_tasks_list == {
        'Draft': [], 
        'To Review': [], 
        'To Be Fixed': [], 
        'To Publish': [{'Title': 'Task 3', 'Content': 'Description of task 3', 'Index': '3182', 'Edit_button_present': True, 'Show_button_present': True}], 
        'Published': []
        }