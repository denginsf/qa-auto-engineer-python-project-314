import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def base_url():
    return os.environ.get('APP_BASE_URL', 'http://localhost:5173')

def test_first(base_url):
    driver = webdriver.Chrome()
    driver.get(base_url)
    enter_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ":r6:"))).send_keys('admin')
    enter_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ":r4:"))).send_keys('admin')
    click_login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/form/div/button'))).click()
    title = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'react-admin-title'))).text
    assert title == 'Welcome to the administration'