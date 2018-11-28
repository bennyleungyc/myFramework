class BasePage(object):

    _driver = None

    def suite_setup(self,msg):
        print("====my_suite_setup")
        print("===={}".format(msg))

    def suite_teardown(self,msg):
        print("====my_suite_teardown")
        print("===={}".format(msg))
