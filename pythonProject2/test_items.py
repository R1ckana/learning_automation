from urllib import request

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test...')
    yield browser
    print('\nquit browser...')
    browser.quit()


class TestMainPage1:
    def test_guest_should_check_basket_link(self, browser):
        browser.get(link)
        browser.find_element(By.LINK_TEXT, 'Добавить в корзину')
        browser.click()
