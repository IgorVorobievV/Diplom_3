from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.login_locators import LoginLocators
from data.data import *

class LoginPage(BasePage):

    def open_login_page(self):
        self.open(ACCOUNT_URL)
        self.lose(BaseLocators.LOADING_MODAL)

    def login(self):
        self.type(LoginLocators.USEREMAIL_INPUT, user_email)
        self.type(LoginLocators.PASSWORD_INPUT, user_password)
        self.click(LoginLocators.SUBMIT_BUTTON)