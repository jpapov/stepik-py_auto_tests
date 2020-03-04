from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import *


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    book_btn = browser.find_element_by_id('book')
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book_btn.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text

    def calc(x):
        return str(log(abs(12*sin(int(x)))))

    summ = calc(x)
    input_text = browser.find_element_by_css_selector('input#answer')
    input_text.send_keys(summ)

finally:

    btn = browser.find_element_by_css_selector('button[type="submit"]')
    btn.click()

