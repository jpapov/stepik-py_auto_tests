import unittest
import time
from selenium import webdriver


class TestRegistration(unittest.TestCase):
    def test_first_link(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # fill field
        input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
        input3.send_keys("w@w.com")

        # submit
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # find element by text
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # write in welcome_text text on element welcome_text_elt
        welcome_text = welcome_text_elt.text

        # check with assert
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(2)
        browser.quit()

    def test_second_link(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # fill field
        input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
        input3.send_keys("w@w.com")

        # submit
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # find element by text
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # write in welcome_text text on element welcome_text_elt
        welcome_text = welcome_text_elt.text

        # check with assert
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(2)
        browser.quit()


if __name__ == '__main__':
    unittest.main()
