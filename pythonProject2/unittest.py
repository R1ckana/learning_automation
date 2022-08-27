from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


link1 = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link1)

firstname = browser.find_element(By.TAG_NAME, 'input.form-control.first')
firstname.send_keys("Ivan")
lastname = browser.find_element(By.TAG_NAME, 'input.form-control.second')
lastname.send_keys("Petrov")
email = browser.find_element(By.TAG_NAME, 'input.form-control.third')
email.send_keys('ivanpetrov@gmail.com')

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link2)

firstname = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
firstname.send_keys("Ivan")
lastname = browser.find_element(By.TAG_NAME, 'input.form-control.second')
lastname.send_keys("Petrov")
email = browser.find_element(By.TAG_NAME, 'input.form-control.third')
email.send_keys('ivanpetrov@gmail.com')

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text2 = welcome_text_elt.text
assert "Congratulations! You have successfully registered!" == welcome_text2


time.sleep(5)
browser.quit()

if __name__ == "__main__":
    pytest.main()
