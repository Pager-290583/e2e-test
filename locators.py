from selenium.webdriver.common.by import By


class Locators:
    AUTH_BUTTON = (By.XPATH, "//p[contains(.,'Личный Кабинет')]")
    REG_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    REG_BUTTON_2 = (By.XPATH, "//button[contains(.,'Зарегистрироваться')]")
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    PASSWORD_PASS = (By.NAME, "Пароль")
    PASSWORD_FAIL = (By.NAME, "Пароль")

    ENTER_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]')
    ENTER_BUTTON_2 = (By.XPATH, '//a[text()="Войти"]')
    INPUT_EMAIL = (By.XPATH, "//input[@type='text']")
    STATIC_PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    '''Index Page'''
    BUTTON_LOGIN_INDEX_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    VALIDATION_TEXT = (By.XPATH, "//button[contains(.,'Оформить заказ')]")

    BUTTON_LOGOUT = (By.XPATH, "//button[contains(.,'Выход')]")
    BUTTON_CONSTRUCTOR = (By.XPATH, "// p[contains(., 'Конструктор')]")
    BUTTON_LOGO = (By.XPATH, "//a[@class='active']")

    '''Тестирование Табов Конструктора'''
    TAB_BULKI = (By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2) > div:nth-child(1) > span")
    TAB_SOUS = (By.XPATH, "//span[text()='Соусы']")
    TAB_NACHINKA = (By.XPATH, "//span[text()='Начинки']")

    HEADER_TEXT_VALIDATION = (By.XPATH, ".//h1[text()='Соберите бургер']")
    TAB_NACHINKI_CLICK = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Начинки']")
    HEADERS_TEXT_NACHINKI = (By.XPATH, "//h2[text()='Булки']")
    TAB_SOUS_CLICK = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Соусы']")
    HEADERS_TEXT_SOUS = (By.XPATH, "//h2[text()='Соусы']")
    TAB_BULKI_CLICK = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Булки']")
    VALIDATION_BULKI2 = (By.CLASS_NAME, "ab_tab_type_current__2BEPc")
    HEADERS_TEXT_BULKI = (By.XPATH, "//h2[text()='Булки']")

    LINK = 'https://stellarburgers.nomoreparties.site/'
    LINK_PROFILE = 'https://stellarburgers.nomoreparties.site/account/profile'
    LINK_LOGIN = '/login'