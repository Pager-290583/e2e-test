from selenium.webdriver.chrome.webdriver import WebDriver
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from test_date.user_data import UserData


class TestRegistrationPass:
    @allure.feature('Регистрация')
    def test_registration(self, driver: WebDriver, user_data: UserData):
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(user_data.name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(user_data.email)
        driver.find_element(*Locators.PASSWORD_PASS).send_keys(user_data.pas)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.REG_BUTTON_2)).click()
        driver.find_element(*Locators.AUTH_BUTTON).click()
        assert Locators.LINK_LOGIN in driver.current_url

