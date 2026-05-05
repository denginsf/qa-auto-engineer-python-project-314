from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.users_page import UsersPage
from pages.statuses_page import StatusesPage
from pages.labels_page import LabelsPage
import time


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
    labels_page.input_status_data('test_label')
    assert labels_page.find_succes_snackbar() == True
    main_page.go_to_labels()
    assert labels_page.is_label_exist('test_label') == True
