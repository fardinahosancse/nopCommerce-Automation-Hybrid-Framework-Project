from selenium.webdriver.common.by import By
from Utility.configReader import readConfig


class PageTitleCollector:
    def __init__(self,driver):
        self.driver = driver

    def Title(self):
        return self.driver.find_element(By.XPATH,readConfig("Locators","title_xpath")).text

    def Current_Title(self):
        return self.driver.find_element(By.XPATH, readConfig("Locators", "Ctitle_xpath")).text

    #For Comparison of Saved or Not

    def EmailData(self):
        return self.driver.find_element(By.XPATH, readConfig("Locators", "emailC_xpath")).text
    def NameData(self):
        return self.driver.find_element(By.XPATH, readConfig("Locators", "nameC_xpath")).text
    def CompanyNameData(self):
        return self.driver.find_element(By.XPATH, readConfig("Locators", "cnameC_xpath")).text
