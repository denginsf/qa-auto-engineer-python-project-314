from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_first(driver, base_url):
    start_page = LoginPage(driver, base_url)
    start_page.open_login_page(base_url)
    start_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'