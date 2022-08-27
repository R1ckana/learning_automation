from selenium.webdriver.common.by import By
import time

link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(30)
    dobavit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    dobavit.checked = dobavit.get_attribute('type')
    assert dobavit.checked == 'submit', 'hz cho tut mozhno napisat'
