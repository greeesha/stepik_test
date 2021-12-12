from selenium import webdriver
import time 

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/alert_accept.html'

with webdriver.Chrome() as browser:
    try:
        browser.get(url)
        
        browser.find_element_by_css_selector("[type='submit']").click()
        confirm = browser.switch_to.alert
        confirm.accept()

        time.sleep(3)

        xxx = browser.find_element_by_id('input_value').text
        
        browser.find_element_by_id('answer').send_keys(calc(xxx))



        browser.find_element_by_css_selector("[type='submit']").click()
        time.sleep(10)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        time.sleep(1)

