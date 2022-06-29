from .base_page import BasePage
from .locators import BasketPageLocators
from .main_page import MainPage


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):   
        # проверяем, что нет товара в корзине
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "There are products in basket, but shouldn't be"
    
    def basket_is_empty(self):
        # ожидаем, что есть сообщение о том, что корзина пуста
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Empty basket message is not presented"
    
    