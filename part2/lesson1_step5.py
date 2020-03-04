from selenium import webdriver
import math


link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_css_selector('div.form-group #input_value')
x = x_element.text


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    y = calc(x)
    input_text = browser.find_element_by_css_selector('div.form-group [type="text"]')
    input_text.send_keys(y)
    checkbox = browser.find_element_by_css_selector('div.form-check [type="checkbox"]')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('div.form-radio-custom [for = "robotsRule"]')
    radiobutton.click()

finally:
    submit_btn = browser.find_element_by_css_selector('button[type="submit"]')
    submit_btn.click()






