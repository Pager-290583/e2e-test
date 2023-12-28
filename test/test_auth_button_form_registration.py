from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from test_date.constants import Constants


class TestLinkAuthFromRegistrationPage:
    def test_auth_from_registration_page(self, driver, user_data):
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.ENTER_BUTTON_2).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.STATIC_PASSWORD).send_keys(Constants.PASSWORD)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()

        assert 'Оформить заказ' == WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.VALIDATION_TEXT))).text

