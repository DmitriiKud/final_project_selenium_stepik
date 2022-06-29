import pytest
from selenium import webdriver
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage


# Временно закомментил

"""
# вводим xfail 
@pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="fixing this bug right now")), 8, 9])

def test_guest_can_add_product_to_basket(browser, number):
    
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    
    page = ProductPage(browser, link) #может использоваться и BasePage
    page.open()
    page.guest_add_to_basket(browser, link) #добавляем книгу в корзину
    page.should_be_proper_bookname() #проверяем, что имя книги соответствует добавленному
    page.should_be_correct_price_in_basket() #проверяем, что стоимость корзины равна стоимости книги
"""

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link, 0) #может использоваться и BasePage
    page.open()
    page.guest_add_to_basket(browser, link) #добавляем книгу в корзину
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link, 0) #может использоваться и BasePage
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link, 0) #может использоваться и BasePage
    page.open()
    page.guest_add_to_basket(browser, link) #добавляем книгу в корзину
    page.should_be_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page():

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_basket_page() # переходим в корзину
    basket_page = BasketPage(browser, browser.current_url) # объявляем переменную для выполнения метода страницы
    basket_page.should_not_be_product_in_basket()
    basket_page.basket_is_empty()