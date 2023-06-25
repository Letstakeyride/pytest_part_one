import pytest
from selene import browser

"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
size_for_windows = [
    (1920, 1080),
    (1600, 1200),
    (1280, 720)
]

size_for_mobile = [
    (450, 900),
    (350, 800),
    (250, 700)
]


@pytest.fixture(params=size_for_windows)
def size_for_windows(request):
    return request.param


def test_github_desktop(size_for_windows):
    browser.open('')
    browser.driver.set_window_size(size_for_windows[0],
                                   size_for_windows[1])
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.fixture(params=size_for_mobile)
def size_for_mobile(request):
    return request.param


def test_github_mobile(size_for_mobile):
    browser.open('')
    browser.driver.set_window_size(size_for_mobile[0],
                                   size_for_mobile[1])
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
