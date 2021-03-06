import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver.WebDriverManager import WebDriverManager
from selenium.webdriver.support.ui import Select
# from utils.screenshot2 import screenshot

class Web(object):

    _driver = None

    def __init__(self, browser):
        self._driver = WebDriverManager.getdriver()
        self._wait = WebDriverWait(self._driver, 10)

    def get_web_element_by_xpath(self, xpath):
        return self._wait.until(EC.presence_of_element_located((By.XPATH,
                                xpath)))

    def get_web_elements_by_xpath(self, xpath):
        return self._wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                xpath)))

    def wait_for_element_visible(self, element):
        return self._wait.until(EC.visibility_of(element))

    def click_element(self, element):
        self.wait_for_element_visible(element)
        element.click()

    def send_key_to_element(self, element, text):
        element.send_keys(text)

    def clear_element_text(self, element):
        element.clear()

    def clear_and_type(self, element, text):
        self.clear_element_text(element)
        self.send_key_to_element(element, text)

    def select_from_dropdown(self, element, text):
        Select(element).select_by_visible_text(text)

    def is_element_displayed(self, element):
        return element.is_displayed()

    def is_element_selected(self, element):
        return element.is_selected()

    def get_text_from_element(self, element):
        return element.text

    def openlink(self, path):
        self._driver.get(path)

    def close_all(self):
        print(self._driver)
        # self.capture_page_screenshot()
        print(os.getcwd() + '/close.png')
        self._driver.get_screenshot_as_file(os.getcwd() + '/close.png')

        self._driver.close()
        self._driver.quit()
        # self._driver.stop()

    def capture_page_screenshot(self):
        ul = BuiltIn().get_library_instance('SeleniumLibrary')
        path = ul.capture_page_screenshot()
        return path
