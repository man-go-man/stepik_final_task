import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# добавляем пользовательский параметр "language" командной строки
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language: ru, en-gb, fr, es, it, etc.")

@pytest.fixture(scope="function")
def language(request):
    lng = request.config.getoption("language")
    if lng is None:
        lng="en"
    return lng

# фикстура для запуска браузера с указанным языком
@pytest.fixture(scope="function")
def browser(request, language):
    print(f"\nstart browser for test with language: {language}")
    options = ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser.")
    browser.quit()