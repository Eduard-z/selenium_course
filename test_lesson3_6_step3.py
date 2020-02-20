import pytest
import time
import math
from selenium import webdriver

links = ['https://stepik.org/lesson/236895/step/1', 
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1']

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))
    print(answer)
    time.sleep(8)
    browser.find_element_by_css_selector("textarea.textarea").send_keys(str(answer))
    time.sleep(3)
    browser.find_element_by_css_selector("button.submit-submission  ").click()
    time.sleep(3)
    assert browser.find_element_by_xpath("//div[@class='attempt__message']/div/pre").text == "Correct!", "Incorrect answer"
