from selene import browser
import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://github.com/'
    browser.open('/')
    yield
    browser.quit()
