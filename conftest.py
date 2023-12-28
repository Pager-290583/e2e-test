import pytest
from selenium import webdriver


from test_date.constants import Constants
from test_date.user_data import UserData


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--headless')  # добавили настройку
    chrome_options.add_argument('--window-size=640,480')  # добавили ещё настройку
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки
    # driver = webdriver.Chrome()
    driver.get(Constants.URL)
    yield driver
    driver.quit()



@pytest.fixture()
def user_data():
    user_data = UserData()
    return user_data

