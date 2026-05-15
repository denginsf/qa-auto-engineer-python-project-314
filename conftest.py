import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.users_page import UsersPage
from pages.tasks_page import TasksPage
from pages.labels_page import LabelsPage
from pages.statuses_page import StatusesPage


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
    opts.add_argument("--disable-gpu")
    opts.add_argument("--headless=new")
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
    if not main_page.is_on_page('Welcome to the administration'):
        raise RuntimeError(f'Login failed. Unexpected page')
    return main_page


@pytest.fixture
def users_page(logged_in_main_page, driver, base_url):
    logged_in_main_page.go_to_users()
    users_page = UsersPage(driver, base_url)
    if not users_page.is_on_page("Users"):
        raise RuntimeError(f'Expected to be on Users page with title "Users", got "{users_page.get_page_title()}"')
    if not users_page.is_on_page_by_url("users"):
        raise RuntimeError(f'URL does not contain "users". Current URL: {users_page.driver.current_url}')
    return users_page


@pytest.fixture
def tasks_page(logged_in_main_page, driver, base_url):
    logged_in_main_page.go_to_tasks()
    tasks_page = TasksPage(driver, base_url)
    if not tasks_page.is_on_page("Tasks"):
        raise RuntimeError(f'Expected to be on Tasks page with title "Tasks", got "{tasks_page.get_page_title()}"')
    if not tasks_page.is_on_page_by_url("tasks"):
        raise RuntimeError(f'URL does not contain "tasks". Current URL: {tasks_page.driver.current_url}')
    return tasks_page


@pytest.fixture
def labels_page(logged_in_main_page, driver, base_url):
    logged_in_main_page.go_to_labels()
    labels_page = LabelsPage(driver, base_url)
    if not labels_page.is_on_page("Labels"):
        raise RuntimeError(f'Expected to be on Tasks page with title "Labels", got "{labels_page.get_page_title()}"')
    if not labels_page.is_on_page_by_url("labels"):
        raise RuntimeError(f'URL does not contain "labels". Current URL: {labels_page.driver.current_url}')
    return labels_page


@pytest.fixture
def statuses_page(logged_in_main_page, driver, base_url):
    logged_in_main_page.go_to_statuses()
    statuses_page = StatusesPage(driver, base_url)
    if not statuses_page.is_on_page("Task statuses"):
        raise RuntimeError(f'Expected to be on Tasks page with title "Task statuses", got "{statuses_page.get_page_title()}"')
    if not statuses_page.is_on_page_by_url("task_statuses"):
        raise RuntimeError(f'URL does not contain "task_statuses". Current URL: {statuses_page.driver.current_url}')
    return statuses_page