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