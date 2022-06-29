import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

# получается упрощенный тест
def test_guest_can_go_to_login_page_from_main_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.got_to_login_page()
    login_page = LoginPage(browser, browser.current_url) # объявляем переменную для выполнения метода страницы
    login_page.should_be_login_page()

# проверяем, что есть ссылка, которая ведет на логин
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_basket_page() # переходим в корзину
    basket_page = BasketPage(browser, browser.current_url) # объявляем переменную для выполнения метода страницы
    basket_page.should_not_be_product_in_basket()
    basket_page.basket_is_empty()
    
