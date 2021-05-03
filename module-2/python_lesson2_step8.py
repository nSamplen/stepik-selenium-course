from selenium import webdriver
import time
import math
import os 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_firstname = browser.find_element_by_css_selector("input[name='firstname']")
    input_firstname.send_keys("Anna")

    input_lastname = browser.find_element_by_css_selector("input[name='lastname']")
    input_lastname.send_keys("Egorova")

    input_email = browser.find_element_by_css_selector("input[name='email']")
    input_email.send_keys("egorova.anna@gmail.com")

    file_element = browser.find_element_by_css_selector("input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file_element.send_keys(file_path)

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