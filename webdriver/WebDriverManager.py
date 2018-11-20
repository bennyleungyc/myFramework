from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverManager(object):

    __driver = None

    @classmethod
    def get_web_driver(cls, browser):
        if cls.__driver is None:
            if (browser.lower()) == "chrome":
                cls.__driver = webdriver.Chrome(ChromeDriverManager().install())

        return cls.__driver