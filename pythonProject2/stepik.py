import time
import pytest
from selenium import webdriver
from math import log
from selenium.webdriver.common.by import By

link = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="function")
def browser():
    print('\nstart browser for test...')
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print('\nquit browser...')
    browser.quit()


class TestMainPage1:

    def test_link0(self, browser):

        browser.get(link[0])
        browser.implicitly_wait(10)
        answer_browser = browser.find_element(By.TAG_NAME, 'textarea')
        answer_browser.send_keys(str(log(int(time.time()))))
        submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
        submit.click()
        correct = browser.find_element(By.TAG_NAME, 'p')
        correct.click()
        assert 'Correct!' in correct.text

        time.sleep(5)

    def test_link1(self, browser):

        browser = webdriver.Chrome()
        browser.get(link[1])
        browser.implicitly_wait(10)
        answer_browser = browser.find_element(By.TAG_NAME, 'textarea')
        answer_browser.send_keys(str(log(int(time.time()))))
        submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
        submit.click()
        correct = browser.find_element(By.TAG_NAME, 'p')
        correct.click()
        assert 'Correct!' in correct.text

        time.sleep(5)

    def test_link2(self, browser):

        browser = webdriver.Chrome()
        browser.get(link[2])
        browser.implicitly_wait(10)
        answer_browser = browser.find_element(By.TAG_NAME, 'textarea')
        answer_browser.send_keys(str(log(int(time.time()))))
        submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
        submit.click()
        correct = browser.find_element(By.TAG_NAME, 'p')
        correct.click()
        assert 'Correct!' in correct.text

        time.sleep(5)

    @pytest.mark.xfail(reason='The owl')
    def test_link3(self, browser):
        browser = webdriver.Chrome()
        browser.get(link[3])
        browser.implicitly_wait(10)
        answer_browser = browser.find_element(By.TAG_NAME, 'textarea')
        answer_browser.send_keys(str(log(int(time.time()))))
        submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
        submit.click()
        correct = browser.find_element(By.TAG_NAME, 'p')
        correct.click()
        assert 'Correct!' in correct.text

        time.sleep(5)
    @pytest.mark.xfail(reason='are not')
    def test_link4(self, browser):
        browser = webdriver.Chrome()
        browser.get(link[4])
        browser.implicitly_wait(10)
        answer_browser = browser.find_element(By.TAG_NAME, 'textarea')
        answer_browser.send_keys(str(log(int(time.time()))))
        submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
        submit.click()
        correct = browser.find_element(By.TAG_NAME, 'p')
        correct.click()
        assert 'Correct!' in correct.text

        time.sleep(5)

    def test_link5(self, browser):
        browser = webdriver.Chrome()
        browser.get(link[5])
        browser.implicitly_wait(10)
        answer_browser = browser.find_element(By.TAG_NAME, 'textarea')
        answer_browser.send_keys(str(log(int(time.time()))))
        submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
        submit.click()
        correct = browser.find_element(By.TAG_NAME, 'p')
        correct.click()
        assert 'Correct!' in correct.text

        time.sleep(5)

    def test_link6(self, browser):
        browser = webdriver.Chrome()
        browser.get(link[6])
        browser.implicitly_wait(10)
        answer_browser = browser.find_element(By.TAG_NAME, 'textarea')
        answer_browser.send_keys(str(log(int(time.time()))))
        submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
        submit.click()
        correct = browser.find_element(By.TAG_NAME, 'p')
        correct.click()
        assert 'Correct!' in correct.text

        time.sleep(5)

    @pytest.mark.xfail(reason='where they seem! 0v0')
    def test_link7(self, browser):
        browser = webdriver.Chrome()
        browser.get(link[7])
        browser.implicitly_wait(10)
        answer_browser = browser.find_element(By.TAG_NAME, 'textarea')
        answer_browser.send_keys(str(log(int(time.time()))))
        submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
        submit.click()
        correct = browser.find_element(By.TAG_NAME, 'p')
        correct.click()
        assert 'Correct!' in correct.text

        time.sleep(5)
