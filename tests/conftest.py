import pytest
from selenium import webdriver
from helpers.user_helper import *


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

@pytest.fixture
def setup_user(driver_setup):
    user_creator = ManipulationUserData()
    user_creator.setup_class()
    user_data = user_creator.create_user()
    yield user_data
    user_creator.teardown_class()