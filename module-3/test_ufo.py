import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

pytest.result_str = ""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print("\n\nResult = "+pytest.result_str)


@pytest.mark.parametrize('lesson', ["236895", "236896", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    
    answer = math.log(int(time.time()))

    textarea = WebDriverWait(browser, 12).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    textarea.send_keys((str)(answer))

    button = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()

    check_answer = WebDriverWait(browser, 12).until(
            EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    
    got_text = check_answer.text

    # to get final result string
    if (got_text != "Correct!"):
        pytest.result_str += got_text


    assert got_text == "Correct!"
    



