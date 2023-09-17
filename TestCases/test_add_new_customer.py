import time
import pytest

from Pages.SP_PageTitleCollector import PageTitleCollector
from TestCases.BaseTest import DRIVER_INITIALIZATION_OVER_ALL_TESTCASE
from Utility.dataProvider import get_data
from Pages.LoginPage import Login

import logging
from Utility.LogUtil import Logger
log = Logger(__name__,logging.INFO)

class Test_ADD_NEW_CUSTOMER(DRIVER_INITIALIZATION_OVER_ALL_TESTCASE):


    @pytest.mark.parametrize("email,password,firstname,lastname,company,admincmnt",get_data("data","../Excel/nopCusData.xlsx"))
    def test_add_new_customer(self,email,password,firstname,lastname,company,admincmnt):
        print("-------------test initialization-------------")
        LoginXL = Login(self.driver)

        #Login---->Go to DashBoard----->Add new customer
        LoginXL.DO_LOGIN_AND_GO_TO_DASHBOARD()\
            .DASHOARD_SELECT_CUSTOMER_FROM_NAVBAR()\
            .ADD_NEW_CUSTOMER()\
            .FILL_ADD_NEW_CUSTOMER_PAGE_FORM(email,password,firstname,lastname,company,admincmnt)
        time.sleep(3)

        Title=PageTitleCollector(self.driver)
        print(Title)
        print(Title.EmailData(),Title.NameData(),Title.CompanyNameData())
        print("-------------Starting Data Verification-------------")
        assert Title.EmailData() == email ,"Email Not Matched"
        log.logger.info(">Verifying Data: " + str(Title.EmailData() + "-VS-" + str(email)))
        assert Title.NameData() == str(firstname+" "+lastname) ,"Name Not Matched"
        log.logger.info(">Verifying Data: " + str(Title.NameData() + "-VS-" + str(firstname+lastname)))
        assert Title.CompanyNameData() == company ,"Company Not Matched"
        print("------------- Verification Complete-------------")









