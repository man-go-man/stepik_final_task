import pytest
from pages.product_page import ProductPage

# после прогона всех тестов помечаем упавший тест меткой xfail (упал 7)
@pytest.mark.parametrize('promo_code', [pytest.param(no, marks=pytest.mark.xfail(no==7, reason='bad promo_code')) for no in range(10)]) # Значение параметра может изменяться от offer0 до offer9
def test_guest_can_add_product_to_basket(browser, promo_code):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_item_name_be_equal_to_item_name_in_basket_msg() # Метод для проверки имени
    page.should_see_basket_value_msg() # Метод для проверки цены