import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture
def base_url():
    implementation = os.getenv("IMPLEMENTATION") 
    if implementation: 
        base_url = f"http://{implementation}.test" 
    else: 
        base_url = os.getenv("APP_BASE_URL", "http://localhost:5173")
    return base_url


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_main_page(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open(base_url)
    login_page.login('admin', 'admin')
    main_page = MainPage(driver, base_url)
    title = main_page.title()
    if main_page.title() != 'Welcome to the administration':
        raise RuntimeError(f'Login failed. Expected title "Welcome to the administration", got "{title}"')
    return main_page