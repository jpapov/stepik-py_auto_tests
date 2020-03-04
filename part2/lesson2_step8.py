from selenium import webdriver
import os


link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    first_name = browser.find_element_by_css_selector('input[name="firstname"]')
    first_name.send_keys('Jerry')
    last_name = browser.find_element_by_css_selector('input[name="lastname"]')
    last_name.send_keys('Papov')
    email = browser.find_element_by_css_selector('input[name="email"]')
    email.send_keys('w@w.ru')
    add_file = browser.find_element_by_css_selector('input#file')
    add_file.send_keys(file_path)

finally:

    btn = browser.find_element_by_css_selector('button[type="submit"]')
    btn.click()
