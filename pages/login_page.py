from .base_page import BasePage
from .locators import LoginPageLocators
from mimesis import Person, Locale  # библиотека для генерации фейковых данных


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login link is not presented" # проверка на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" # проверка наличия формы логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented" # проверка наличия формы регистрации

    def register_new_user(self):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        register_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        person = Person(Locale.EN) # инициализация персоны
        email = person.email() # генерация мыла
        password = person.password(length=9) # генерация пароля
        register_email.send_keys(email)
        register_password.send_keys(password)
        register_password_confirm.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()