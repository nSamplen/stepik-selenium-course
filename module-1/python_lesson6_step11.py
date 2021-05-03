from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link2)
    #elements = browser.find_elements_by_tag_name("input[required]")
    #for element in elements:
    #    element.send_keys("М")

    input1 = browser.find_element_by_css_selector("div.first_block div.form-group input.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block div.form-group input.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block div.form-group input.third")
    input3.send_keys("IvanPetrov@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла