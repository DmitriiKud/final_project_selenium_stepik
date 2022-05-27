import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

# выделяем открытие страницы регистрации в отдельное действие    
def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

# получается упрощенный тест
def test_guest_can_go_to_login_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.got_to_login_page()
    login_page = LoginPage(browser, browser.current_url) # выполняем метод страницы - переходим на страницу логина
    login_page.should_be_login_page()

# проверяем, что есть ссылка, которая ведет на логин
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()














# старая версия
"""def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click() 

def test_guest_can_go_to_login_page(browser): 
   browser.get(link) 
   go_to_login_page(browser)"""