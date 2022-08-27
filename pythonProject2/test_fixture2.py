from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

link = 'https://selenium1py.pythonanywhere.com/'

@pytest.fixture()
def browser():
    print('\nstart browser for test...')
    browser = webdriver.Chrome()
    return browser

class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')