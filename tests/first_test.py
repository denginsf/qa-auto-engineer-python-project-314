from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.users_page import UsersPage


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


def test_create_user(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.open_user_creation_form() == True
    users_page.input_user_data('test@test.com', 'Alex', 'Test')
    assert users_page.find_succes_snackbar() == True
    main_page.go_to_users()
    first_name, last_name = users_page.get_user_data_by_email('test@test.com')
    assert first_name == 'Alex'
    assert last_name == 'Test'


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
    users_page.save_user()
    assert users_page.find_error_snackbar()
    assert users_page.get_required_errors_count() == 3
    users_page.input_user_data('test', 'Ivan', 'Doe')
    assert users_page.email_validation_error_is_visible() == True
    users_page.delete_user_email()
    users_page.enter_user_email('john_changed@google.com')
    users_page.save_user()
    first_name, last_name = users_page.get_user_data_by_email('john_changed@google.com')
    assert first_name == 'Ivan'
    assert last_name == 'Doe'
    assert users_page.find_user_updated_snackbar()


def test_user_delete(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    users_page.click_on_row('john@google.com')
    users_page.delete_user()
    assert users_page.find_delete_snackbar()
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
    users_page.delete_user()
    assert users_page.find_all_users_deleted_snackbar()
    assert users_page.users_table_is_empty() == True