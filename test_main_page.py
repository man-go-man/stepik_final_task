from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем объект Page Object
    page.open()                           # открываем страницу в браузере
    page.go_to_login_page()      # выполняем метод страницы — переходим на страницу логина