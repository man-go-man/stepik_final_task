import pytest

from pages.basket_page import BasketPage
from pages.product_page import ProductPage

# после прогона всех тестов помечаем упавший тест меткой xfail (упал 7)
@pytest.mark.parametrize('promo_code', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='bad promo_code')) for i in range(10)]) # Значение параметра может изменяться от offer0 до offer9
def test_guest_can_add_product_to_basket(browser, promo_code):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()  # ожидаем, что там нет сообщения об успешном добавлении в корзину
    page.add_item_to_basket()
    page.solve_quiz_and_get_code() #Посчитать результат математического выражения и ввести ответ
    page.should_item_name_be_equal_to_item_name_in_basket_msg() # Метод для проверки имени
    page.should_see_basket_value_msg() # Метод для проверки цены
    # page.success_message_should_disappear()  # элемент присутствует на странице и должен исчезнуть (на самом деле не должен)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page_from_product_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open() # Гость открывает страницу товара
    page.go_to_basket() # Переходит в корзину по кнопке в шапке
    basket_page = BasketPage(browser, browser.current_url) # страницу корзины инициализируем в теле теста
    basket_page.should_not_see_any_items_in_basket()  # Ожидаем, что в корзине нет товаров
    basket_page.should_see_empty_basket_text()  # Ожидаем, что есть текст о том что корзина пуста