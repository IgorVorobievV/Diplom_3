from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.base_locators import BaseLocators
from data.data import *

class OrderFeedPage(BasePage):
    
    def open_order_feed_page(self):
        self.open(ORDER_FEED_URL)
        self.lose(BaseLocators.LOADING_MODAL)

    def get_text_alltime_counter(self):
        return self.get_text(OrderFeedLocators.ALLTIME_ORDERS_COUNT)
    
    def get_text_today_counter(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNT) 
    
    def сollect_ready_orders_list(self):
        return self.сollect_states(OrderFeedLocators.READY_ORDERS_ITEM, 5, 0.1)
    
