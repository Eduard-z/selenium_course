from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    check = browser.find_element_by_id('robotCheckbox')
    check.click()

    button = browser.find_element_by_class_name('btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла