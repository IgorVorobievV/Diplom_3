from selenium.webdriver.common.by import By

class LoginLocators:
    USEREMAIL_INPUT = (By.XPATH, ".//label[contains(text(),'Email')]/parent::div/input")
    PASSWORD_INPUT = (By.XPATH, ".//label[contains(text(),'Пароль')]/parent::div/input")
    SUBMIT_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти')]")
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]")
    ACCOUNT_BUTTON = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]")
    CHECK_BUTTON = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")