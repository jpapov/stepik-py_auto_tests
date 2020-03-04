from selenium import webdriver
from math import sin, log

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('span#input_value')
x = x_element.text



def calc(x):
    return str(log(abs(12*sin(int(x)))))


try:

    summ = calc(x)
    # browser.execute_script("return argumets[0].scrollIntoView;")
    browser.execute_script("window.scrollBy(0, 100);")
    input_text = browser.find_element_by_css_selector('input#answer')
    input_text.send_keys(summ)
    check_box = browser.find_element_by_css_selector('input.form-check-input#robotCheckbox')
    check_box.click()
    radio_btn = browser.find_element_by_css_selector('input.form-check-input#robotsRule')
    radio_btn.click()

finally:
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()

