from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestRegistrationLenPassword:
    def test_registration_len_password(self, driver, user_data):
        driver.find_element(*Locators.AUTH_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(user_data.name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(user_data.email)
        driver.find_element(*Locators.PASSWORD_FAIL).send_keys(user_data.pas_fail)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.REG_BUTTON_2)).click()
        error = driver.find_element(By.CSS_SELECTOR, ".input__error").text
        assert error == 'Некорректный пароль'