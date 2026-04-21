from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.base_page import BasePage
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
    users_page.create_user('test@test.com', 'Alex', 'Test')
    assert users_page.find_succes_snackbar() == True
    main_page.go_to_users()
    first_name, last_name = users_page.get_user_data_by_email('test@test.com')
    assert first_name == 'Alex'
    assert last_name == 'Test'