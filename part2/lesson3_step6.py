from selenium import webdriver
from math import *
from time import sleep


link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    troll_btn = browser.find_element_by_css_selector('button.trollface')
    troll_btn.click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text

    def calc(x):
        return str(log(abs(12*sin(int(x)))))

    summ = calc(x)

    input_text = browser.find_element_by_css_selector('input#answer')
    input_text.send_keys(summ)

finally:
    submit_btn = browser.find_element_by_css_selector('button[type = "submit"]')
    submit_btn.click()


