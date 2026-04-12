from pages.base_page import BasePage
from locators.main_locators import MainLocators
from locators.base_locators import BaseLocators
from data.data import *

class MainPage(BasePage):

    def open_main_page(self):
        self.open(BASE_URL)
        self.lose(BaseLocators.LOADING_MODAL)

    def find_page_h1(self):
        return self.find(BaseLocators.H1).text
    
    def click_first_ingredient_in_buns(self):
        self.click(MainLocators.INGREDIENTS_BUN)

    def find_detail_modal(self):
        return self.find(MainLocators.DETAIL_MODAL)
    
    def click_detail_modal_close_button(self):
        self.click(MainLocators.DETAIL_MODAL_CLOSE_BUTTON)
    
    def lose_detail_modal(self):
        return self.lose(MainLocators.DETAIL_MODAL)
    
    def add_first_bun_in_basket(self):
        self.drag_and_drop_js(MainLocators.INGREDIENTS_BUN, MainLocators.CONSTRUCTOR_BASKET_LIST)
        #self.loading(BaseLocators.LOADING_MODAL)

    def get_text_first_bun_counter(self):
        return self.get_text(MainLocators.INGREDIENTS_BUN_COUNTER)

    def click_basket_button(self):
        self.click(MainLocators.CONSTRUCTOR_BASKET_BUTTON)

    def check_order(self):
        self.loading(BaseLocators.LOADING_MODAL)

    def get_order_id(self):
        return int(self.get_text(MainLocators.ORDER_MODAL_TITLE))
    
    def click_order_modal_close_button(self):
        self.click(MainLocators.ORDER_MODAL_CLOSE_BUTTON)