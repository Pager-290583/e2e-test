from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from test_date.constants import Constants


class TestLogoutFromMyPageAccount:
    def test_auth_button_cabinet(self, driver, user_data):
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.STATIC_PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.AUTH_BUTTON)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGOUT)).click()
        assert Locators.LINK_PROFILE in driver.current_url
