from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    checkbox1 = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox1.click()

    roundbtn = browser.find_element_by_css_selector("#robotsRule")
    roundbtn.click()

    button = browser.find_element_by_tag_name("button")
    button.click()


        # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла