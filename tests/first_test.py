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


def test_create_user(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.open_entity_creation_form()
    users_page.input_user_data('test@test.com', 'Alex', 'Test')
    assert users_page.find_success_snackbar()
    logged_in_main_page.go_to_users()
    user_data = users_page.get_user_data_by_email('test@test.com')
    assert user_data == {'id': '9', 'first_name': 'Alex', 'last_name': 'Test', 'createdAt': 'Дата задана'}


def test_smoke_users_list(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    assert users_page.users_table_is_loaded()
    all_users_data = users_page.get_all_users_data()
    assert all_users_data == [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'createdAt': '30.10.2023, 03:00:00'}, 
        {'id': '2', 'first_name': 'Jack', 'last_name': 'Jons', 'createdAt': '30.10.2023, 03:00:00'}, 
        {'id': '3', 'first_name': 'Jane', 'last_name': 'Smith', 'createdAt': '05.11.2023, 03:00:00'}, 
        {'id': '4', 'first_name': 'Alice', 'last_name': 'Johnson', 'createdAt': '06.11.2023, 03:00:00'}, 
        {'id': '5', 'first_name': 'Peter', 'last_name': 'Brown', 'createdAt': '07.11.2023, 03:00:00'}, 
        {'id': '6', 'first_name': 'Sarah', 'last_name': 'Wilson', 'createdAt': '08.11.2023, 03:00:00'}, 
        {'id': '7', 'first_name': 'Michael', 'last_name': 'Davis', 'createdAt': '09.11.2023, 03:00:00'}, 
        {'id': '8', 'first_name': 'Emily', 'last_name': 'Martinez', 'createdAt': '10.11.2023, 03:00:00'}
        ]
    

def test_user_update_validations(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.click_on_row('john@google.com')
    users_page.delete_user_email()
    users_page.delete_user_first_name()
    users_page.delete_user_last_name()
    users_page.save_entity()
    assert users_page.find_error_snackbar()
    assert users_page.get_required_errors_count() == 3
    users_page.input_user_data('test', 'Ivan', 'Doe')
    assert users_page.email_validation_error_is_visible()


def test_user_update(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.click_on_row('john@google.com')
    users_page.delete_user_email()
    users_page.delete_user_first_name()
    users_page.delete_user_last_name()
    users_page.input_user_data('john_changed@google.com', 'Ivan', 'Doe')
    assert users_page.find_updated_snackbar()
    user_data = users_page.get_user_data_by_email('john_changed@google.com')
    assert user_data == {'id': '1', 'first_name': 'Ivan', 'last_name': 'Doe', 'createdAt': 'Дата задана'}


def test_user_delete(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.click_on_row('john@google.com')
    users_page.delete_entity()
    assert users_page.find_deleted_snackbar()
    assert not users_page.is_user_exist('john@google.com')


def test_all_users_delete(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.select_all_entities()
    users_page.delete_entity()
    assert users_page.find_all_entities_deleted_snackbar()
    assert users_page.users_table_is_empty()


def test_create_status(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    statuses_page.open_entity_creation_form()
    statuses_page.input_status_data('test_status', 'test')
    assert statuses_page.find_success_snackbar()
    logged_in_main_page.go_to_statuses()
    status_data = statuses_page.get_status_data_by_name('test_status')
    assert status_data == {'id': '6', 'slug': 'test', 'createdAt': 'Дата задана'}


def test_smoke_statuses_list(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    assert statuses_page.statuses_table_is_loaded()
    all_statuses_data = statuses_page.get_all_statuses_data()
    assert all_statuses_data == [
        {'id': '1', 'name': 'Draft', 'slug': 'draft', 'createdAt': '30.10.2023, 03:00:00'}, 
        {'id': '2', 'name': 'To Review', 'slug': 'to_review', 'createdAt': '30.10.2023, 03:00:00'}, 
        {'id': '3', 'name': 'To Be Fixed', 'slug': 'to_be_fixed', 'createdAt': '30.10.2023, 03:00:00'}, 
        {'id': '4', 'name': 'To Publish', 'slug': 'to_publish', 'createdAt': '30.10.2023, 03:00:00'}, 
        {'id': '5', 'name': 'Published', 'slug': 'published', 'createdAt': '30.10.2023, 03:00:00'}
        ]


def test_status_update_validations(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    statuses_page.click_on_status_row('Draft')
    statuses_page.delete_status_name()
    statuses_page.delete_status_slug()
    statuses_page.save_entity()
    assert statuses_page.find_error_snackbar()
    assert statuses_page.get_required_errors_count() == 2


def test_status_update(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    statuses_page.click_on_status_row('Draft')
    statuses_page.delete_status_name()
    statuses_page.delete_status_slug()
    statuses_page.input_status_data('test_updated', 'updated')
    assert statuses_page.find_updated_snackbar()
    status_data = statuses_page.get_status_data_by_name('test_updated')
    assert status_data == {'id': '1', 'slug': 'updated', 'createdAt': 'Дата задана'}


def test_status_delete(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    statuses_page.click_on_status_row('Draft')
    statuses_page.delete_entity()
    assert statuses_page.find_deleted_snackbar()
    assert not statuses_page.is_status_exist('Draft')


def test_all_statuses_delete(driver, base_url, logged_in_main_page):
    logged_in_main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    statuses_page.select_all_entities()
    statuses_page.delete_entity()
    assert statuses_page.find_all_entities_deleted_snackbar()
    assert statuses_page.statuses_table_is_empty()


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
    assert labels_page.find_success_snackbar() == True
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
    labels_page.select_all_entities()
    labels_page.delete_entity()
    assert labels_page.find_all_entities_deleted_snackbar()
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
    assert tasks_page.find_success_snackbar() == True
    assert tasks_page.get_task_id_value() == '16'
    main_page.go_to_tasks()
    assert tasks_page.is_task_present_in_satus('Draft', 'Test task') == True

def test_update_task(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_tasks()
    tasks_page = TasksPage(driver, base_url)
    tasks_page.start_task_edit_by_name('Task 11')
    tasks_page.change_assignee('emily@example.com')
    tasks_page.change_title('Changed')
    tasks_page.change_content('Changed content')
    tasks_page.change_status('Published')
    tasks_page.add_label('task')
    tasks_page.save_entity()
    assert tasks_page.find_updated_snackbar()
    tasks_page.filter_by_assignee('emily@example.com')
    tasks_list = tasks_page.get_all_statuses_data()
    assert tasks_list == {
        'Draft': [], 
        'To Review': [], 
        'To Be Fixed': [], 
        'To Publish': [], ''
        'Published': [{'Title': 'Changed', 'Content': 'Changed content', 'Index': '3220', 'Edit_button_present': True, 'Show_button_present': True}]
        }

def test_delete_task(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_tasks()
    tasks_page = TasksPage(driver, base_url)
    tasks_page.start_task_edit_by_name('Task 14')
    tasks_page.delete_entity()
    assert tasks_page.find_deleted_snackbar()
    assert tasks_page.is_task_present_in_satus('To Publish', 'Task 14') == False