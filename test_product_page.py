import pytest
from selenium import webdriver
from .pages.product_page import ProductPage

# вводим xfail 
@pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="fixing this bug right now")), 8, 9])

def test_guest_can_add_product_to_basket(browser, number):
    
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    
    page = ProductPage(browser, link) #может использоваться и BasePage
    page.open()
    page.guest_add_to_basket(browser, link) #добавляем книгу в корзину
    page.should_be_proper_bookname() #проверяем, что имя книги соответствует добавленному
    page.should_be_correct_price_in_basket() #проверяем, что стоимость корзины равна стоимости книги


