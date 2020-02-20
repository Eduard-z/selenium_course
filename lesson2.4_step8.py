from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 
	price = WebDriverWait(browser, 12).until(
			EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

	book = browser.find_element_by_id("book")
	book.click()

	x_element = browser.find_element_by_id('input_value')
	x = x_element.text
	y = calc(x)

	input = browser.find_element_by_id('answer')
	input.send_keys(y)

	submit = browser.find_element_by_id('solve')
	submit.click()
finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла