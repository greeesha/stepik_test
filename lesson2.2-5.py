from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

with webdriver.Chrome() as browser:
    try:
        browser.get(link)

        xxx = browser.find_element_by_id('input_value').text   
        browser.find_element_by_id('answer').send_keys(calc(xxx))

        option1 = browser.find_element_by_id('robotCheckbox')
        browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
        option1.click()
        
        option2 = browser.find_element_by_id('robotsRule')
        browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
        option2.click()

        button = browser.find_element_by_tag_name("button")
        button.click()
        time.sleep(10)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        time.sleep(1)

