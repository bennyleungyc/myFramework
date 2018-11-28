from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverManager(object):

    __driver = None

    def __init__(self, browser):
        if self.__driver is None:
            if (browser.lower()) == "chrome":
                self.__driver = webdriver.Chrome(ChromeDriverManager().install())
                # self.__driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    @classmethod
    def setdriver(cls, browser):
        if cls.__driver is None:
            if (browser.lower()) == "chrome":
                cls.__driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def getdriver(cls):
        return cls.__driver

    @property
    def web_driver(self):
        return self.__driver
