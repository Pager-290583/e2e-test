from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from test_date.constants import Constants


class TestOpenLinkKonstruktorLinkInedx:
    def test_auth_click_account_click_konstr_click_index(self, driver, user_data):
        driver.find_element(*Locators.BUTTON_LOGIN_INDEX_PAGE).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.STATIC_PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.AUTH_BUTTON))
        driver.find_element(*Locators.BUTTON_LOGO).click()
        elm = driver.find_element(*Locators.VALIDATION_TEXT).text
        assert elm == 'Оформить заказ'
