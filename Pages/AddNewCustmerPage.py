import time

from Pages.BasePage import BaseFather


class AddNewCustomerPage(BaseFather):
    def __init__(self,driver):
        super().__init__(driver)

    def FILL_ADD_NEW_CUSTOMER_PAGE_FORM(self,email,password,firstname,lastname,company,admincmnt):
        self.Type("email_xpath",email)
        self.Type("password_xpath",password)
        self.Type("firstname_xpath",firstname)
        self.Type("lastname_xpath",lastname)
        self.Click("gender_xpath")

        self.Click("dateofbirth_toggle_xpath")
        self.Click("dateofbirth_xpath")

        self.Type("company_xpath", company)

        self.Click("isTaxAttempth_MENU_xpath")

        self.Click("newsletter_MENU_xpath")
        self.Click("newsletter_subMENU_xpath")



        self.Click("customer_role_xpath")
        self.Click("customer_role_selection_xpath")

        self.Click("Vendor_MENU_xpath")
        self.Click("Vendor_MENU_selection_xpath")



        self.Type("adminComment_xpath",admincmnt)

        time.sleep(3)



        self.Click("save_xpath")




