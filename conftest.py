import pytest
from selenium import webdriver


from test_date.constants import Constants
from test_date.user_data import UserData


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)
    yield driver
    driver.quit()



@pytest.fixture()
def user_data():
    user_data = UserData()
    return user_data

