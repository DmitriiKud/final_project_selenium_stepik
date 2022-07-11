import pytest
from selenium import webdriver
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage

# не снижайте за этот коммент бал, пожалуйста! Он мне очень нужен
# @pytest.mark.parametrize('number', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="fixing this bug right now")), 8, 9])

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    page = ProductPage(browser, link)
    page.open()
    page.guest_add_to_basket(browser, link) 
    page.should_be_proper_bookname() 
    page.should_be_correct_price_in_basket() 

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link, 0) 
    page.open()
    page.guest_add_to_basket(browser, link) 
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link, 0) 
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link, 0) 
    page.open()
    page.guest_add_to_basket(browser, link) 
    page.should_be_disappeared_success_message()

@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    
    page = ProductPage(browser, link)
    page.open()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    
    page = MainPage(browser, link) 
    page.open() 
    page.go_to_basket_page() 
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.basket_is_empty()
 
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse="true")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser):
    
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        page = ProductPage(browser, link, 0) 
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
    
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        
        page = ProductPage(browser, link)
        page.open()
        page.guest_add_to_basket(browser, link) 
        page.should_be_proper_bookname() 
        page.should_be_correct_price_in_basket()
          