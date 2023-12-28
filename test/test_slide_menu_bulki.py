from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestClickAllTabValidation:

    def test_slide_menu_bulki(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_TEXT_VALIDATION))

        driver.find_element(*Locators.TAB_NACHINKI_CLICK).click()
        driver.find_element(*Locators.TAB_BULKI_CLICK).click()
        assert driver.find_element(*Locators.HEADERS_TEXT_BULKI).is_displayed()
