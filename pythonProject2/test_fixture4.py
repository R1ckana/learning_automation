# открывает браузер только один раз. надо бы понять что тут что значит.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture(scope='class')
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав её как параметр
    def test_guest_should_see_login_link(self, browser):
        print('start test')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')
        print('finish test')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('start test 2')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
        print('finish test 2')
