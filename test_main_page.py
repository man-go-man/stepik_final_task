import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем объект Page Object
    page.open()                           # открываем страницу в браузере
    page.go_to_login_page()      # выполняем метод страницы — переходим на страницу логина
    # login_page = page.go_to_login_page() # 3/3 Первый способ перехода: сохранив возвращаемое значение в переменную в def go_to_login_page(self) в MainPage, мы можем использовать методы новой страницы в тесте
    login_page = LoginPage(browser, browser.current_url) # 1/2 Второй подход: переход между страницами происходит неявно, страницу инициализируем в теле теста
    login_page.should_be_login_page() # 2/2 Второй подход: переход между страницами происходит неявно, страницу инициализируем в теле теста

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url) # страницу корзины инициализируем в теле теста
    basket_page.should_not_see_any_items_in_basket() # Ожидаем, что в корзине нет товаров
    basket_page.should_see_empty_basket_text() # Ожидаем, что есть текст о том что корзина пуста