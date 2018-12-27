from webdriver.Web import Web
from utils.pagefactory_support import cacheable, callable_find_by as find_by


class PurchaseTicketPage(object):

    _name_textbox = find_by(id_="address")
    _flight_title = find_by(xpath="//h2")

    def __init__(self, browser):
        print('PurchaseTicketPage====init')
        self._web = Web(browser)

    def input_name(self, name):
        self._web.send_key_to_element(self._name_textbox(), name)

    def get_title_content(self):
        print(self._web.get_web_element_by_xpath('//h2').text)
        return self._web.get_text_from_element(self._flight_title())
