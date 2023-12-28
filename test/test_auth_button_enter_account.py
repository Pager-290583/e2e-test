from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from test_date.constants import Constants


class TestAuthIndexPage:
    def test_auth_button_cabinet(self, driver, user_data):
        driver.find_element(*Locators.BUTTON_LOGIN_INDEX_PAGE).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.STATIC_PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.VALIDATION_TEXT)).click()
        elm = driver.find_element(*Locators.VALIDATION_TEXT).text
        assert elm == 'Оформить заказ'

