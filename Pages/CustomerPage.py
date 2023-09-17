from Pages.AddNewCustmerPage import AddNewCustomerPage
from Pages.BasePage import BaseFather


class Customer(BaseFather):
    def __init__(self, driver):
        super().__init__(driver)

    def ADD_NEW_CUSTOMER(self):
        # CLICK TO GOTO ADD NEW CUSTOMER
        self.Click("add_new_customer_xpath")
        return AddNewCustomerPage(self.driver)
