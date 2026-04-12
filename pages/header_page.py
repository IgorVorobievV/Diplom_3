from pages.base_page import BasePage
from locators.header_locators import HeaderLocators

class HeaderPage(BasePage):
    
    def click_constructor_link(self):
        self.click(HeaderLocators.CONSTRUCTOR_LINK)     
   
    def click_order_feed_link(self):
        self.click(HeaderLocators.ORDER_FEED_LINK)

    def click_account_link(self):
        self.click(HeaderLocators.ACCOUNT_LINK)
        

    