from webdriver.WebDriverManager import WebDriverManager


class BasePage(object):

    _driver = None

    def suite_setup(self, browser):
        WebDriverManager.setdriver(browser)
        print("====my_suite_setup")

    def suite_teardown(self,msg):
        print("====my_suite_teardown")
        print("===={}".format(msg))
