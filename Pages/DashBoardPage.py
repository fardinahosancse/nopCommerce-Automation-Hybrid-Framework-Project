from Pages.BasePage import BaseFather
from Pages.CustomerPage import Customer


class DashBoard(BaseFather):
    def __init__(self, driver):
        super().__init__(driver)

    def DASHOARD_SELECT_CUSTOMER_FROM_NAVBAR(self):
        #Nav Menu
        self.Click("customer_dropdown_xpath_firefox")

        #Select Customer
        self.Click("customer_dropdown_submenu_xpath_firefox")
        return Customer(self.driver)