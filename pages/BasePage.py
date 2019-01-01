from webdriver.WebDriverManager import WebDriverManager
from webdriver.Web import Web
from config import DEFAULT_BASE_URL

class BasePage(object):

    _driver = None
    _web = None
    _browser = None

    def __init__(self, browser):
        print('BasePage====init')
        # WebDriverManager.setdriver(browser)
        # self._web = Web(browser)
        print(browser)
        self._browser = browser

    def openbrowser(self):
        print('BasePage====open')
        WebDriverManager.setdriver(self._browser)
        self._web = Web(self._browser)
        self._web.openlink(DEFAULT_BASE_URL)

    def closebrowser(self):
        self._web.close_all()
