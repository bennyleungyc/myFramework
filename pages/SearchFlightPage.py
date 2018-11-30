from webdriver.Web import Web
from utils.pagefactory_support import cacheable, callable_find_by as find_by


class SearchFlightPage(object):

    __url = "http://blazedemo.com/"
    _click_button = find_by(xpath="//input[@type='submit']")

    def open(self):
        print('SearchFlightPage====open')
        self._web.open(self.__url)

    def __init__(self, browser):
        print('SearchFlightPage====init')
        self._web = Web(browser)

    def select_departure_city(self, city):
        self._web.get_web_element_by_xpath("//select[@name='fromPort']/option[@value='{}']".format(city)).click()

    def select_destination_city(self, city):
        self._web.get_web_element_by_xpath("//select[@name='toPort']/option[@value='{}']".format(city)).click()

    def search_for_flights(self):
        # self._web.get_web_element_by_xpath("//input[@type='submit']").click()
        self._click_button().click()

    def get_found_flights(self):
        return self._web.get_web_elements_by_xpath("//table[@class='table']/tbody/tr")

    def close(self):
        self._web.close_all()
