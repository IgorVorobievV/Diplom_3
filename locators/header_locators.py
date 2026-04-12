from selenium.webdriver.common.by import By

class HeaderLocators:
    ACCOUNT_LINK = (By.XPATH, ".//p[contains(text(),'Личный Кабинет')]/..")
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[contains(text(),'Конструктор')]/..")
    ORDER_FEED_LINK = (By.XPATH, ".//p[contains(text(),'Лента Заказов')]/..")