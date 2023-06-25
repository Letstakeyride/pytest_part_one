import pytest
from selene import browser

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

windows_size = [
    (1920, 1080),
    (1600, 1200),
    (1280, 720),
    (450, 900),
    (350, 800),
    (250, 700)
]


@pytest.fixture(params=windows_size)
def windows_size(request):
    return request.param


def test_github_desktop(windows_size):
    browser.open('')
    browser.driver.set_window_size(windows_size[0],
                                   windows_size[1])
    if windows_size[0] < 768:
        pytest.skip(reason="Разрешение не подходит для вашего устройства")
    else:
        browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(windows_size):
    browser.open('')
    browser.driver.set_window_size(windows_size[0],
                                   windows_size[1])
    if windows_size[0] > 768:
        pytest.skip(reason="Разрешение не подходит для вашего устройства")
    else:
        browser.element('.flex-column [aria-label="Toggle navigation"]').click()
