import allure
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

class TestHeader:
    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Проверить, что по клику на «Конструктор» открывается страница с конструктором') 
    def test_click_constructor_link_wright_h1(self, driver):
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        with allure.step('Открываем страницу личного кабинета'):
            login_page.open_login_page()

        with allure.step('Кликаем на «Конструктор»'):
            header_page.click_constructor_link()
            
        with allure.step('Проверяем наличие заголовка конструктора'):
            assert main_page.find_page_h1() == 'Соберите бургер'

    @allure.title('Переход по клику на раздел «Лента заказов»')
    @allure.description('Проверить, что по клику на «Лента заказов» открывается страница с заказами') 
    def test_click_order_feed_link_wright_h1(self, driver):
        with allure.step('Создаем объект.'):
            header_page = HeaderPage(driver)
            main_page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            main_page.open_main_page()

        with allure.step('Кликаем на «Лента заказов»'):
            header_page.click_order_feed_link()
            
        with allure.step('Проверяем наличие заголовка ленты заказов'):
            assert main_page.find_page_h1() == 'Лента заказов'