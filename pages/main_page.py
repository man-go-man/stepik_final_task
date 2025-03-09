from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage # 1/3 Первый способ перехода между страницами: сделать импорт страницы с логином

# Класс MainPage - наследник класса BasePage (класс-предок указывается в скобках)
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # символ * указывает на то, что мы передали кортеж(!) для распаковки
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) # 2/3 Первый способ перехода между страницами: возвращать нужный Page Object.

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"