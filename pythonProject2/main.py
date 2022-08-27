from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return log(abs(12 * sin(int(x))))


    book_element = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_element.click()
    x_element_find = browser.find_element(By.ID, 'input_value')
    x_element_find.click()
    x = x_element_find.text
    y = calc(x)
    x_element = browser.find_element(By.ID, 'answer')
    x_element.send_keys(y)

    # Проверяем, что смогли зарегистрироваться ждем загрузки страницы
    button = browser.find_element(By.ID, 'button')
    button.click()
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




#Попробуем реализовать один из автотестов из предыдущего шага.
#Вам дана страница(ссылка в коде.) с формой регистрации.
#Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля, отмеченные символом *: First name, last name, email.
#Текст для полей может быть любым.
#Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!" с текстом на странице,
# которая открывается после регистрации.
#Для сравнения воспользуемся стандартной конструкцией assert из языка Python.