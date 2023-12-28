from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from test_date.constants import Constants


class TestOpenLinkMyAccount:

    def test_open_my_account(self, driver, user_data):
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_PASS).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        text = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.VALIDATION_TEXT))).text
        assert text == 'Оформить заказ'

