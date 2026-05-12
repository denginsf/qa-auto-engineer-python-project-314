import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage

@pytest.fixture
def base_url():
    return os.environ.get('APP_BASE_URL', 'http://localhost:5173')

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_main_page(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open(base_url)
    login_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    assert main_page.title() == 'Welcome to the administration'
    return main_page