from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDERS_DATA_BASE = ".//div[contains(@class, 'ordersData')]"
    READY_ORDERS_LIST = (By.XPATH, f"{ORDERS_DATA_BASE}//ul[contains(@class, 'orderListReady')]")
    READY_ORDERS_ITEM = (By.XPATH, f"{ORDERS_DATA_BASE}//ul[contains(@class, 'orderListReady')]/li")
    READY_ORDERS_EMPTY_ITEM = (By.XPATH, f"{ORDERS_DATA_BASE}//ul[contains(@class, 'orderListReady')]/li[contains(text(), 'Все текущие заказы готовы!')]")
    ALLTIME_ORDERS_COUNT = (By.XPATH, f"{ORDERS_DATA_BASE}//p[contains(text(), 'за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, f"{ORDERS_DATA_BASE}//p[contains(text(), 'за сегодня')]/following-sibling::p")