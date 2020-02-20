from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import os

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    find_the_sum = str(int(num1)+int(num2))
    select3 = Select(browser.find_element_by_id('dropdown'))
    select3.select_by_value(find_the_sum)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    #time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()