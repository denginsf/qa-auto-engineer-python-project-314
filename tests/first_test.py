from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.base_page import BasePage


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