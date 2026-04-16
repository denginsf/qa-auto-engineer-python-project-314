import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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