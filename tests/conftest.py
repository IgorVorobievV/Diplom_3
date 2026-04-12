import pytest
from selenium import webdriver

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser_name = request.param

    if browser_name == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    yield driver
    driver.quit()