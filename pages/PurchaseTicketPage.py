from webdriver.Web import Web
from utils.pagefactory_support import cacheable, callable_find_by as find_by


class PurchaseTicketPage(object):

    _name_textbox = find_by(id_="address")

    def __init__(self, browser):
        print('PurchaseTicketPage====init')
        self._web = Web(browser)

    def input_name(self, name):
        self._web.send_key_to_element(self._name_textbox(), name)


