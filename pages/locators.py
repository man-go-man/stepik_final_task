from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_URL = (By.ID, 'login_link')
    LOGIN_FORM = (By.ID,'login_form')
    REGISTER_FORM = (By.ID,'register_form')

class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_BTN = (By.CSS_SELECTOR, 'span>a')
    ITEM_NAME = (By.CSS_SELECTOR, 'h1:nth-child(1)')
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, 'div.alertinner strong') # первый блок с названием найдётся
    BASKET_VALUE_MSG = (By.CSS_SELECTOR, 'div.alertinner p strong') # сумма корзины в сообщении