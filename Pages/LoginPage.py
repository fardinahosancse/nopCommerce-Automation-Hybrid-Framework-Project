from Pages.BasePage import BaseFather
from Pages.DashBoardPage import DashBoard


class Login(BaseFather):
    def __init__(self, driver):
        super().__init__(driver)

    def DO_LOGIN_AND_GO_TO_DASHBOARD(self):
        # Click on login
        self.Click("login_xpath")
        return DashBoard(self.driver)
