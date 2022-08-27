# этот файл - фикстура. он нужен для того чтобы эту фикстуру можно было использовать в любом файле этого проекта.
# создаётся в корневой директории.
# чтобы использовать в другом файле, в функции, в качестве аргумента используется название функции которая здесь.
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='None', help='Choose languages: es or fr')

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='None', help='Choose browser chrome or firefox')

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('languages')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser_name = request.config.getoption('browser_name')
    yield browser
    browser.quit()
