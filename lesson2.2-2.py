from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

with webdriver.Chrome() as browser:
    try:
        browser.get(link)

        num1 = browser.find_element_by_id('num1').text
        num2 = browser.find_element_by_id('num2').text
        summ = int(num1)+int(num2)
        print(summ)
        
        from selenium.webdriver.support.ui import Select
        Select(browser.find_element_by_tag_name("select")).select_by_value(str(summ))

        button = browser.find_element_by_tag_name("button")
        button.click()
        time.sleep(10)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        time.sleep(1)

