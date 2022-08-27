from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import *
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return log(abs(12 * sin(int(x))))

    browser.implicitly_wait(5) #"неявное ожидание" - ищет каждый элемент 5 секунд. страхует от задержек на сайте.
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify"))) # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной.
    button2 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#"), "искомый текст")) #ждать появления нужного текста.
    x_element_find = browser.find_element(By.TAG_NAME, 'img#treasure')
    x_element_find.get_attribute()
    x = x_element_find.text
    y = calc(x)
    x_element = browser.find_element(By.TAG_NAME, 'input#answer.form-control')
    x_element.send_keys(y)
    checkbox = browser.find_element(By.TAG_NAME, 'input#robotCheckbox.form-check-input')
    checkbox.click()
    radiobutton = browser.find_element(By.TAG_NAME, 'input#robotsRule.form-check-input')
    radiobutton.click()
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')  # примерCSS селектора
    alert = browser.switch_to.alert  # найти окно вверху браузера
    alert.accept()  # нажать ок. в алёрте только одна кнопка.
    alert_text = alert.text  # чтобы получить текст из алёрта
    confirm = browser.switch_to.alert  # конфирм - окно вверху браузера с двумя вариантами ответа
    confirm.accept()  # принять конфирм
    confirm.dismiss()  # отклонить конфирм
    prompt = browser.switch_to.alert  # промпт - окно в которое нужно ввести символы
    prompt.send_keys("My answer")  # собственно, отправление "ключей"
    prompt.accept()  # отправить "ключи"
    current_dir = os.path.abspath(os.path.dirname(__file__)) #файл должен лежать в одной папке с проектом.
    file_path = os.path.join(current_dir, 'название файла.txt') #создаём переменную
    x_element.send_keys(file_path) #отправка файла
    browser.execute_script("alert('Hello')") #для того чтобы вызывать алёрт
    browser.switch_to.window(window_name='chrome') #переключить на новое окно браузера
    new_window = browser.window_handles[1] #получить имя вкладки
    first_window = browser.window_handles[0]#за одно получить имя старой вкладки, дабы иметь возможность вернуться к ней.
    #после переключения, код будет работать с новой вкладкой
    message = browser.find_element(By.ID, "verify_message") #находим элемент, по которому надо проверить текст
    assert "successful" in message.text #непосредственно проверка текста

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# Попробуем реализовать один из автотестов из предыдущего шага.
# Вам дана страница(ссылка в коде.) с формой регистрации.
# Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля, отмеченные символом *: First name, last name, email.
# Текст для полей может быть любым.
# Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!" с текстом на странице,
# которая открывается после регистрации.
# Для сравнения воспользуемся стандартной конструкцией assert из языка Python.
