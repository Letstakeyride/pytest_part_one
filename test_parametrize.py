import pytest
from selene import browser

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""


@pytest.fixture(scope='function')
def manager_browser(request):
    resolutions = {
        'desktop': (1280, 720),
        'mobile': (250, 700)
    }
    return resolutions[request.param]


@pytest.mark.parametrize('manager_browser', ['desktop'], indirect=True)
def test_github_desktop(manager_browser):
    browser.driver.set_window_size(*manager_browser)
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('manager_browser', ['mobile'], indirect=True)
def test_github_mobile(manager_browser):
    browser.driver.set_window_size(*manager_browser)
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
