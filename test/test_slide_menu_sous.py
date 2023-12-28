from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestClickTabBulki:
    def test_slide_menu_sous(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_TEXT_VALIDATION))

        driver.find_element(*Locators.TAB_SOUS_CLICK).click()
        assert driver.find_element(*Locators.HEADERS_TEXT_SOUS).is_displayed()