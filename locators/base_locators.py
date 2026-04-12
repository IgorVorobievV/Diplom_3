from selenium.webdriver.common.by import By

class BaseLocators:
    H1 = (By.XPATH, ".//h1")
    LOADING_MODAL = (By.XPATH, ".//img[contains(@class, 'modal__loading')]/..")