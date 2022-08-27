import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke  # это маркировки тестов
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    @pytest.mark.regression  # маркировки тест, забавная штука
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')

    # снизу тест, который заранее упадёт. "reason" это причина по, которой он упал. запуск -rx
    @pytest.mark.xfail(reason='this test with bad response')
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'button.favorite')

    @pytest.mark.xfail(reason='this test with good response')
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'input.btn.btn-default')
