import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome', 'firefox'])
def driver_setup(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    yield driver
    driver.quit()
