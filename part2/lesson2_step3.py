from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

browser.get(link)
x_element = browser.find_element_by_css_selector('span#num1')
x = x_element.text
y_element = browser.find_element_by_css_selector('span#num2')
y = y_element.text


def calc(x, y):
    return str(int(x)+int(y))

try:

    summ = calc(x, y)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(summ)

finally:

    submit_btn = browser.find_element_by_css_selector('button[type="submit"]')
    submit_btn.click()

