from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):

    # проверяем, что страница логина
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Login URL is incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register link is not presented"
        
    def register_new_user(self):
        # регистрирует нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password = "Mayweather"
        email_address = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS)
        email_address.send_keys(email)
        user_password1 = self.browser.find_element(*LoginPageLocators.USER_PASSWORD1)
        user_password1.send_keys(password)
        user_password2 = self.browser.find_element(*LoginPageLocators.USER_PASSWORD2)
        user_password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        time.sleep(3) #чтобы все успело прогрузиться