from selenium import webdriver
from math import *


link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    first_btn = browser.find_element_by_css_selector('button[type="submit"]')
    first_btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector('span#input_value')
    x = x_element.text

    def calc(x):
        return str(log(abs(12*sin(int(x)))))

    summ = calc(x)

    input_text = browser.find_element_by_css_selector('input#answer')
    input_text.send_keys(summ)

finally:
    btn = browser.find_element_by_css_selector('button[type="submit"]')
    btn.click()
