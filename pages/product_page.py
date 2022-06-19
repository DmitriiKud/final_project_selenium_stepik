from .base_page import BasePage
from .locators import ProductPageLocators
from .main_page import MainPage
import time

class ProductPage(MainPage):
    
    # метод для добавления товара в корзину
    def guest_add_to_basket(self, browser, link):
        
        page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET) # находим кнопку добавить в корзину
        basket.click()
        #time.sleep(2)
        BasePage.solve_quiz_and_get_code(self)
    
    def should_be_proper_bookname(self):

        bookname = self.browser.find_element(*ProductPageLocators.ADDED_BOOKNAME)
        wanted_bookname = self.browser.find_element(*ProductPageLocators.BOOKNAME)
        assert bookname.text == wanted_bookname.text, "Wrong book added"
        print(f"{wanted_bookname.text} in the basket")
        #time.sleep(1)
    
    def should_be_correct_price_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert price.text == price_in_basket.text, "Price incorrect in the basket"
        print(f"Price {price_in_basket.text} is correct")
        #time.sleep(1)