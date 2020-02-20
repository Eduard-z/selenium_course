from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    name1 = browser.find_element_by_name('firstname')
    name1.send_keys('name1')
    name2 = browser.find_element_by_name('lastname')
    name2.send_keys('name2')
    name3 = browser.find_element_by_name('email')
    name3.send_keys('email')
    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    # добавляем к этому пути имя файла (в той же папке)
    file_path = os.path.join(current_dir, 'test_doc.txt') 
    element = browser.find_element_by_name('file')
    element.send_keys(file_path)
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
    browser.quit()