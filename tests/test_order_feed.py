import allure
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

class TestMain:
    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    @allure.description('Сравниваем счётчик «Выполнено за всё время» до заказа и после')
    def test_alltime_counter_new_order_counter_incremented(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Открываем страницу «Лента заказов»'):
            order_feed_page.open_order_feed_page()

        with allure.step('Находим счётчик «Выполнено за всё время» и сохраняем его содержание'):
            counter = int(order_feed_page.get_text_alltime_counter())

        main_page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            main_page.open_main_page()
        
        with allure.step('Добавляем первую в списке булку в корзину'):
            main_page.add_first_bun_in_basket()

        with allure.step('Кликаем на кнопку "Войти в аккаунт" в корзине'):
            main_page.click_basket_button()

        login_page = LoginPage(driver)

        with allure.step('Авторизуемся'):
            login_page.login()

        with allure.step('Кликаем на кнопку "Оформить заказ" в корзине'):
            main_page.click_basket_button()

        with allure.step('Ждем регистрацию заказа'):
            main_page.check_order()
        
        with allure.step('Кликаем на крестик'):
            main_page.click_order_modal_close_button()

        with allure.step('Открываем страницу «Лента заказов»'):
            order_feed_page.open_order_feed_page()
            
        with allure.step('Проверяем, что счётчик «Выполнено за всё время» стал больше'):
            assert int(order_feed_page.get_text_alltime_counter()) > counter

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    @allure.description('Сравниваем счётчик «Выполнено за сегодня» до заказа и после')
    def test_today_counter_new_order_counter_incremented(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Открываем страницу «Лента заказов»'):
            order_feed_page.open_order_feed_page()

        with allure.step('Находим счётчик «Выполнено за сегодня» и сохраняем его содержание'):
            counter = int(order_feed_page.get_text_today_counter())

        main_page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            main_page.open_main_page()
        
        with allure.step('Добавляем первую в списке булку в корзину'):
            main_page.add_first_bun_in_basket()

        with allure.step('Кликаем на кнопку "Войти в аккаунт" в корзине'):
            main_page.click_basket_button()

        login_page = LoginPage(driver)

        with allure.step('Авторизуемся'):
            login_page.login()

        with allure.step('Кликаем на кнопку "Оформить заказ" в корзине'):
            main_page.click_basket_button()

        with allure.step('Ждем регистрацию заказа'):
            main_page.check_order()
        
        with allure.step('Кликаем на крестик'):
            main_page.click_order_modal_close_button()

        with allure.step('Открываем страницу «Лента заказов»'):
            order_feed_page.open_order_feed_page()
            
        with allure.step('Проверяем, что счётчик «Выполнено сегодня» стал больше'):
            assert int(order_feed_page.get_text_today_counter()) > counter

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    @allure.description('После оформления заказа запоминаем его номер, собираем содержание списка раздела «В работе» в течении 10 секунд с интервалом 0,1 секунда, проверяем вхождение номера заказа в собранный список')
    def test_order_id_new_order_order_id_in_list(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            main_page.open_main_page()
        
        with allure.step('Добавляем первую в списке булку в корзину'):
            main_page.add_first_bun_in_basket()

        with allure.step('Кликаем на кнопку "Войти в аккаунт" в корзине'):
            main_page.click_basket_button()

        login_page = LoginPage(driver)

        with allure.step('Авторизуемся'):
            login_page.login()

        with allure.step('Кликаем на кнопку "Оформить заказ" в корзине'):
            main_page.click_basket_button()

        with allure.step('Ждем регистрацию заказа'):
            main_page.check_order()

        with allure.step('Сохраняем номер заказа'):
            number = str(main_page.get_order_id())

        with allure.step('Кликаем на крестик'):
            main_page.click_order_modal_close_button()

        order_feed_page = OrderFeedPage(driver)

        with allure.step('Открываем страницу «Лента заказов»'):
            order_feed_page.open_order_feed_page()
            
        with allure.step('Проверяем, что номер заказа есть в списке'):
            assert any(number in element for element in order_feed_page.сollect_ready_orders_list())
