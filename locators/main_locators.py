from selenium.webdriver.common.by import By

class MainLocators:
    INGREDIENTS_BASE = ".//section[contains(@class, 'BurgerIngredients_ingredients')]"
    INGREDIENTS_BASE_TITLE = (By.XPATH, f"{INGREDIENTS_BASE}//h1[contains(text(), 'Соберите бургер')]")
    INGREDIENTS_BUNS_LINK = (By.XPATH, f"{INGREDIENTS_BASE}//span[contains(text(), 'Булки')]/..")
    INGREDIENTS_FILLINGS_LINK = (By.XPATH, f"{INGREDIENTS_BASE}//span[contains(text(), 'Начинки')]/..")
    INGREDIENTS_BUN = (By.XPATH, f"{INGREDIENTS_BASE}//h2[contains(text(), 'Булки')]/following-sibling::ul[contains(@class, 'ingredients__list')]/a")
    INGREDIENTS_BUN_COUNTER = (By.XPATH, f"{INGREDIENTS_BASE}//h2[contains(text(), 'Булки')]/following-sibling::ul[contains(@class, 'ingredients__list')]/a//p[contains(@class, 'counter__num')]")

    CONSTRUCTOR_BASKET_BASE = ".//section[contains(@class, 'BurgerConstructor_basket')]"
    CONSTRUCTOR_BASKET = (By.XPATH, CONSTRUCTOR_BASKET_BASE)
    CONSTRUCTOR_BASKET_LIST = (By.XPATH, f"{CONSTRUCTOR_BASKET_BASE}//ul[contains(@class, 'basket__list')]")
    #Перетяните булочку сюда
    CONSTRUCTOR_BASKET_NO_BUN_ITEM = (By.XPATH, f"{CONSTRUCTOR_BASKET_BASE}//span[contains(text(), 'Перетяните булочку сюда')]")
    CONSTRUCTOR_BASKET_BUTTON = (By.XPATH, f"{CONSTRUCTOR_BASKET_BASE}//button")
  
    DETAIL_MODAL_BASE = ".//section[contains(@class, 'Modal_modal')]//h2[contains(text(), 'Детали ингредиента')]/../.."
    DETAIL_MODAL = (By.XPATH, DETAIL_MODAL_BASE)
    DETAIL_MODAL_INGREDIENT_P = (By.XPATH, f"{DETAIL_MODAL_BASE}//p[contains(@class, text')]")
    DETAIL_MODAL_CLOSE_BUTTON = (By.XPATH, f"{DETAIL_MODAL_BASE}//button[contains(@class, 'modal__close')]")

    ORDER_MODAL_BASE = ".//section[contains(@class, 'Modal_modal')]//p[contains(text(), 'идентификатор заказа')]/../.."
    ORDER_MODAL = (By.XPATH, ORDER_MODAL_BASE)
    ORDER_MODAL_TITLE = (By.XPATH, f"{ORDER_MODAL_BASE}//h2")
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, f"{ORDER_MODAL_BASE}//button[contains(@class, 'modal__close')]")
