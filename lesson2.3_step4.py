from selenium import webdriver
import time
import math

def calc(x):
  	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_tag_name("button")
	button.click()

	alert = browser.switch_to.alert
	alert.accept()

	x_element = browser.find_element_by_id('input_value')
	x = x_element.text
	y = calc(x)

	input = browser.find_element_by_id('answer')
	input.send_keys(y)

	submit = browser.find_element_by_class_name('btn')
	submit.click()
finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла