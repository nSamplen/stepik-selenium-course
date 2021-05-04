from selenium import webdriver
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class TestRequiredElements(unittest.TestCase):
    def test_required1(self):
        browser = webdriver.Chrome()
        browser.get(link1)

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
        #assert "Congratulations! You have successfully registered!" == welcome_text

        # закрываем браузер после всех манипуляций
        browser.quit()

        # не забываем оставить пустую строку в конце файла
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        
    def test_required2(self):
        browser = webdriver.Chrome()
        browser.get(link2)

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

        browser.quit()

        # не забываем оставить пустую строку в конце файла
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        
if __name__ == "__main__":
    unittest.main()



