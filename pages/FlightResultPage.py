from webdriver.Web import Web
from utils.pagefactory_support import cacheable, callable_find_by as find_by


class FlightResultPage(object):

    _choose_flight_button = find_by(xpath="//input[@type='submit']")

    def __init__(self, browser):
        print('FlightResultPage====init')
        self._web = Web(browser)

    def choose_flight(self):
        self._web.click_element(self._choose_flight_button())


