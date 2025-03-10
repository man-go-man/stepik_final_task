from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_URL = (By.ID, 'login_link')
    LOGIN_FORM = (By.ID,'login_form')
    REGISTER_FORM = (By.ID,'register_form')