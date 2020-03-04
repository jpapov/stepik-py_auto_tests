
from selenium import webdriver
import math


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_css_selector('img#treasure')
x = x_element.get_attribute('valuex')


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    y = calc(x)
    input_text = browser.find_element_by_css_selector('input#answer')
    input_text.send_keys(y)
    checkbox = browser.find_element_by_css_selector('input.check-input#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('input.check-input#robotsRule')
    radiobutton.click()

finally:
    submit_btn = browser.find_element_by_css_selector('button[type="submit"]')
    submit_btn.click()

