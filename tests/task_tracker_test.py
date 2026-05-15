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


def test_logout(driver, base_url, logged_in_main_page):
    logged_in_main_page.logout()
    login_page = LoginPage(driver, base_url)
    assert login_page.find_lock_icon()


def test_create_user(users_page, logged_in_main_page):
    users_page.open_entity_creation_form()
    assert users_page.get_page_title() == "Create User"
    users_page.input_user_data('test@test.com', 'Alex', 'Test')
    assert users_page.find_success_snackbar()
    logged_in_main_page.go_to_users()
    assert users_page.get_page_title() == "Users"
    user_data = users_page.get_user_data_by_email('test@test.com')
    assert user_data == {'id': '9', 'first_name': 'Alex', 'last_name': 'Test'}


def test_smoke_users_list(users_page, logged_in_main_page):
    assert users_page.users_table_is_loaded()
    assert users_page.get_page_title() == "Users"
    all_users_data = users_page.get_all_users_data()
    assert all_users_data == [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'createdAt': '10/30/2023, 12:00:00 AM'}, 
        {'id': '2', 'first_name': 'Jack', 'last_name': 'Jons', 'createdAt': '10/30/2023, 12:00:00 AM'}, 
        {'id': '3', 'first_name': 'Jane', 'last_name': 'Smith', 'createdAt': '11/5/2023, 12:00:00 AM'}, 
        {'id': '4', 'first_name': 'Alice', 'last_name': 'Johnson', 'createdAt': '11/6/2023, 12:00:00 AM'}, 
        {'id': '5', 'first_name': 'Peter', 'last_name': 'Brown', 'createdAt': '11/7/2023, 12:00:00 AM'}, 
        {'id': '6', 'first_name': 'Sarah', 'last_name': 'Wilson', 'createdAt': '11/8/2023, 12:00:00 AM'}, 
        {'id': '7', 'first_name': 'Michael', 'last_name': 'Davis', 'createdAt': '11/9/2023, 12:00:00 AM'}, 
        {'id': '8', 'first_name': 'Emily', 'last_name': 'Martinez', 'createdAt': '11/10/2023, 12:00:00 AM'}
    ]
    

def test_user_update_validations(users_page, logged_in_main_page):
    users_page.click_on_row('john@google.com')
    assert users_page.get_page_title() == "User john@google.com"
    users_page.delete_user_email()
    users_page.delete_user_first_name()
    users_page.delete_user_last_name()
    users_page.save_entity()
    assert users_page.find_error_snackbar()
    assert users_page.get_required_errors_count() == 3
    users_page.input_user_data('test', 'Ivan', 'Doe')
    assert users_page.email_validation_error_is_visible()


def test_user_update(users_page, logged_in_main_page):
    users_page.click_on_row('john@google.com')
    assert users_page.get_page_title() == "User john@google.com"
    users_page.delete_user_email()
    users_page.delete_user_first_name()
    users_page.delete_user_last_name()
    users_page.input_user_data('john_changed@google.com', 'Ivan', 'Doe')
    assert users_page.find_updated_snackbar()
    user_data = users_page.get_user_data_by_email('john_changed@google.com')
    assert users_page.get_page_title() == "Users"
    assert user_data == {'id': '1', 'first_name': 'Ivan', 'last_name': 'Doe'}


def test_user_delete(users_page, logged_in_main_page):
    users_page.click_on_row('john@google.com')
    assert users_page.get_page_title() == "User john@google.com"
    users_page.delete_entity()
    assert users_page.find_deleted_snackbar()
    assert not users_page.is_user_exist('john@google.com')
    assert users_page.get_page_title() == "Users"


def test_all_users_delete(users_page, logged_in_main_page):
    users_page.select_all_entities()
    users_page.delete_entity()
    assert users_page.find_all_entities_deleted_snackbar()
    assert users_page.users_table_is_empty()
    assert users_page.get_page_title() == "Users"


def test_create_status(statuses_page, logged_in_main_page):
    statuses_page.open_entity_creation_form()
    assert statuses_page.get_page_title() == "Create Task status"
    statuses_page.input_status_data('test_status', 'test')
    assert statuses_page.find_success_snackbar()
    logged_in_main_page.go_to_statuses()
    status_data = statuses_page.get_status_data_by_name('test_status')
    assert statuses_page.get_page_title() == "Task statuses"
    assert status_data == {'id': '6', 'slug': 'test', 'createdAt': 'Дата задана'}


def test_smoke_statuses_list(statuses_page, logged_in_main_page):
    assert statuses_page.statuses_table_is_loaded()
    all_statuses_data = statuses_page.get_all_statuses_data()
    assert statuses_page.get_page_title() == "Task statuses"
    assert all_statuses_data == [
        {'id': '1', 'name': 'Draft', 'slug': 'draft', 'createdAt': '10/30/2023, 12:00:00 AM'}, 
        {'id': '2', 'name': 'To Review', 'slug': 'to_review', 'createdAt': '10/30/2023, 12:00:00 AM'}, 
        {'id': '3', 'name': 'To Be Fixed', 'slug': 'to_be_fixed', 'createdAt': '10/30/2023, 12:00:00 AM'}, 
        {'id': '4', 'name': 'To Publish', 'slug': 'to_publish', 'createdAt': '10/30/2023, 12:00:00 AM'}, 
        {'id': '5', 'name': 'Published', 'slug': 'published', 'createdAt': '10/30/2023, 12:00:00 AM'}
    ]


def test_status_update_validations(statuses_page, logged_in_main_page):
    statuses_page.click_on_status_row('Draft')
    assert statuses_page.get_page_title() == "Task status Draft"
    statuses_page.delete_status_name()
    statuses_page.delete_status_slug()
    statuses_page.save_entity()
    assert statuses_page.find_error_snackbar()
    assert statuses_page.get_required_errors_count() == 2


def test_status_update(statuses_page, logged_in_main_page):
    statuses_page.click_on_status_row('Draft')
    assert statuses_page.get_page_title() == "Task status Draft"
    statuses_page.delete_status_name()
    statuses_page.delete_status_slug()
    statuses_page.input_status_data('test_updated', 'updated')
    assert statuses_page.find_updated_snackbar()
    status_data = statuses_page.get_status_data_by_name('test_updated')
    assert statuses_page.get_page_title() == "Task statuses"
    assert status_data == {'id': '1', 'slug': 'updated', 'createdAt': 'Дата задана'}


def test_status_delete(statuses_page, logged_in_main_page):
    statuses_page.click_on_status_row('Draft')
    assert statuses_page.get_page_title() == "Task status Draft"
    statuses_page.delete_entity()
    assert statuses_page.find_deleted_snackbar()
    assert not statuses_page.is_status_exist('Draft')
    assert statuses_page.get_page_title() == "Task statuses"


def test_all_statuses_delete(statuses_page, logged_in_main_page):
    statuses_page.select_all_entities()
    statuses_page.delete_entity()
    assert statuses_page.find_all_entities_deleted_snackbar()
    assert statuses_page.statuses_table_is_empty()
    assert statuses_page.get_page_title() == "Task statuses"


def test_create_label(labels_page, logged_in_main_page):
    labels_page.open_entity_creation_form()
    assert labels_page.get_page_title() == "Create Label"
    labels_page.input_label_data('test_label')
    assert labels_page.find_success_snackbar()
    logged_in_main_page.go_to_labels()
    label_data = labels_page.get_label_data_by_name('test_label')
    assert labels_page.get_page_title() == "Labels"
    assert label_data == {'id': '6', 'name': 'test_label'}


def test_smoke_labels_list(labels_page, logged_in_main_page):
    assert labels_page.labels_table_is_loaded()
    labels_list = labels_page.get_all_labels_data()
    assert labels_page.get_page_title() == "Labels"
    assert labels_list == [
        {"id": "1", "name": "bug", "createdAt": "12/21/2023, 12:00:00 AM"},
        {"id": "2", "name": "feature", "createdAt": "12/21/2023, 12:00:00 AM"},
        {"id": "3", "name": "enhancement", "createdAt": "12/22/2023, 12:00:00 AM"},
        {"id": "4", "name": "task", "createdAt": "12/23/2023, 12:00:00 AM"},
        {"id": "5", "name": "critical", "createdAt": "12/24/2023, 12:00:00 AM"}
    ]


def test_label_update_validation(labels_page, logged_in_main_page):
    labels_page.click_on_label_row('task')
    assert labels_page.get_page_title() == "Label task"
    labels_page.delete_label_name()
    labels_page.save_entity()
    assert labels_page.find_error_snackbar()
    assert labels_page.get_required_errors_count() == 1


def test_update_label(labels_page, logged_in_main_page):
    labels_page.click_on_label_row('task')
    assert labels_page.get_page_title() == "Label task"
    labels_page.input_label_data('updated_label')
    assert labels_page.find_updated_snackbar()
    label_data = labels_page.get_label_data_by_name('updated_label')
    assert label_data == {'id': '4', 'name': 'updated_label'}
    assert labels_page.get_page_title() == "Labels"


def test_label_delete(labels_page, logged_in_main_page):
    labels_page.click_on_label_row('feature')
    assert labels_page.get_page_title() == "Label feature"
    labels_page.delete_entity()
    assert labels_page.find_deleted_snackbar()
    assert not labels_page.is_label_exist('feature')
    assert labels_page.get_page_title() == "Labels"


def test_all_labels_delete(labels_page, logged_in_main_page):
    labels_page.select_all_entities()
    labels_page.delete_entity()
    assert labels_page.find_all_entities_deleted_snackbar()
    assert labels_page.labels_table_is_empty()
    assert labels_page.get_page_title() == "Labels"


def test_create_task(tasks_page, logged_in_main_page):
    assert tasks_page.open_entity_creation_form()
    assert tasks_page.get_page_title() == "Create Task"
    tasks_page.create_task('emily@example.com', 'Test task', 'Test Content', 'Draft', 'critical')
    assert tasks_page.find_success_snackbar()
    assert tasks_page.get_task_id_value() == '16'
    logged_in_main_page.go_to_tasks()
    task_data = tasks_page.get_task_data_by_name('Test task')
    assert tasks_page.get_page_title() == "Tasks"
    assert task_data == {'Title': 'Test task', 'Content': 'Test Content', 'Edit_button_present': True, 'Show_button_present': True}


def test_update_task(tasks_page, logged_in_main_page):
    tasks_page.start_task_edit_by_name('Task 11')
    assert tasks_page.get_page_title() == "Task Task 11"
    tasks_page.change_assignee('emily@example.com')
    tasks_page.change_title('Changed')
    tasks_page.change_content('Changed content')
    tasks_page.change_status('Published')
    tasks_page.add_label('task')
    tasks_page.save_entity()
    assert tasks_page.find_updated_snackbar()
    tasks_page.filter_by_assignee('emily@example.com')
    tasks_list = tasks_page.get_all_tasks_data()
    assert tasks_page.get_page_title() == "Tasks"
    assert tasks_list == {
        'Draft': [], 
        'To Review': [], 
        'To Be Fixed': [], 
        'To Publish': [],
        'Published': [{'Title': 'Changed', 'Content': 'Changed content', 'Index': '3220', 'Edit_button_present': True, 'Show_button_present': True}]
        }


def test_task_creation_form_validation(tasks_page, logged_in_main_page):
    assert tasks_page.open_entity_creation_form()
    assert tasks_page.get_page_title() == "Create Task"
    assert tasks_page.is_save_button_disabled()
    tasks_page.change_content('Changed content')
    assert not tasks_page.is_save_button_disabled()
    tasks_page.save_entity()
    assert tasks_page.find_error_snackbar()
    assert tasks_page.get_required_errors_count() == 3


def test_smoke_tasks_list(tasks_page, logged_in_main_page):
    assert tasks_page.task_page_is_loaded()
    tasks_list = tasks_page.get_all_tasks_data()
    assert tasks_page.get_page_title() == "Tasks"
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


def test_tasks_filtration_list(tasks_page, logged_in_main_page):
    assert tasks_page.task_page_is_loaded()
    tasks_page.filter_by_assignee('jack@yahoo.com')
    assert tasks_page.get_page_title() == "Tasks"
    filtered_tasks_list = tasks_page.get_all_tasks_data()
    assert filtered_tasks_list == {
        'Draft': [], 
        'To Review': [{'Title': 'Task 12', 'Content': 'Description of task 12', 'Index': '3230', 'Edit_button_present': True, 'Show_button_present': True}], 
        'To Be Fixed': [{'Title': 'Task 13', 'Content': 'Description of task 13', 'Index': '3240', 'Edit_button_present': True, 'Show_button_present': True}], 
        'To Publish': [{'Title': 'Task 3', 'Content': 'Description of task 3', 'Index': '3182', 'Edit_button_present': True, 'Show_button_present': True}, 
                       {'Title': 'Task 14', 'Content': 'Description of task 14', 'Index': '3250', 'Edit_button_present': True, 'Show_button_present': True}], 
        'Published': [{'Title': 'Task 4', 'Content': 'Description of task 4', 'Index': '3203', 'Edit_button_present': True, 'Show_button_present': True}]
        }
    tasks_page.filter_by_status('To Publish')
    filtered_tasks_list = tasks_page.get_all_tasks_data()
    assert filtered_tasks_list == {
        'Draft': [], 
        'To Review': [], 
        'To Be Fixed': [], 
        'To Publish': [{'Title': 'Task 3', 'Content': 'Description of task 3', 'Index': '3182', 'Edit_button_present': True, 'Show_button_present': True}, 
                    {'Title': 'Task 14', 'Content': 'Description of task 14', 'Index': '3250', 'Edit_button_present': True, 'Show_button_present': True}], 
        'Published': []
        }
    tasks_page.filter_by_label('bug')
    filtered_tasks_list = tasks_page.get_all_tasks_data()
    assert filtered_tasks_list == {
        'Draft': [], 
        'To Review': [], 
        'To Be Fixed': [], 
        'To Publish': [{'Title': 'Task 3', 'Content': 'Description of task 3', 'Index': '3182', 'Edit_button_present': True, 'Show_button_present': True}], 
        'Published': []
        }


def test_delete_task(tasks_page, logged_in_main_page):
    tasks_page.start_task_edit_by_name('Task 14')
    assert tasks_page.get_page_title() == "Task Task 14"
    tasks_page.delete_entity()
    assert tasks_page.find_deleted_snackbar()
    assert not tasks_page.is_task_present_in_status('To Publish', 'Task 14')
    assert tasks_page.get_page_title() == "Tasks"