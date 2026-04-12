import allure
from pages.main_page import MainPage

class TestMain:
    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Проверить, что по клику на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_open_detail_modal(self, driver):
        
        with allure.step('Создаем объект.'):
            page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            page.open_main_page()

        with allure.step('Кликаем на первую в списке булку'):
            page.click_first_ingredient_in_buns()
            
        with allure.step('Проверяем наличие окна с деталями'):
            assert page.find_detail_modal() is not None

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @allure.description('Проверить, что всплывающее окно становится не видимым после клика по крестику')
    def test_click_close_button_close_detail_modal(self, driver):
        
        with allure.step('Создаем объект.'):
            page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            page.open_main_page()

        with allure.step('Кликаем на первую в списке булку'):
            page.click_first_ingredient_in_buns()

        with allure.step('Кликаем на крестик'):
            page.click_detail_modal_close_button()
            
        with allure.step('Проверяем невидимость окна с деталями'):
            assert page.lose_detail_modal() is not None

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('Проверить, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_add_ingredient_incremented_counter(self,driver):
        
        with allure.step('Создаем объект.'):
            page = MainPage(driver)

        with allure.step('Открываем главную страницу'):
            page.open_main_page()

        with allure.step('Сохраняем счетчик первой булки'):
            counter = int(page.get_text_first_bun_counter())

        with allure.step('Добавляем первую в списке булку в корзину'):
            page.add_first_bun_in_basket()

        with allure.step('Проверяем, что счетчик увеличился'):
            assert int(page.get_text_first_bun_counter()) > counter
