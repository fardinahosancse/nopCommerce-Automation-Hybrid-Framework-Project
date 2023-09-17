from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from Utility.LogUtil import Logger
log = Logger(__name__,logging.INFO)
from Utility import configReader as CONF


class BaseFather:
    def __init__(self, driver):
        self.driver = driver

    # CLICK:LOCATORS CLICK EXECUTION
    def Click(self, syntex):

        xpath_locator = CONF.readConfig("Locators", syntex)
        element = WebDriverWait(self.driver, 90).until(
            EC.element_to_be_clickable((By.XPATH, xpath_locator))
        )

        element.click()
        log.logger.info(">Clicking on a Element: " + str(syntex))

        #self.driver.find_element(By.XPATH, CONF.readConfig("Locators", syntex)).click()

        # CLICK:LOCATORS CLICK EXECUTION

    def Click_cnditional(self, syntex,expected_text):
        xpath_locator = (By.XPATH,CONF.readConfig("Locators", syntex))
        element = WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element(xpath_locator, expected_text)
        )

        element.click()

        # self.driver.find_element(By.XPATH, CONF.readConfig("Locators", syntex)).click()

    # TYPE:INPUT FIELD TYPER
    def Type(self, syntex, syntex_value):

        xpath_locator = CONF.readConfig("Locators", syntex)
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath_locator))
        )
        element.send_keys(syntex_value)
        log.logger.info(">Typing on a Element: " + str(syntex + "---" + str(syntex_value)))

        #self.driver.find_element(By.XPATH, CONF.readConfig("Locators", syntex)).send_keys(syntex_value)

    # DROPDOWN: SLECTOR FROM DROPDOWN
    def Selection(self, syntex):
        Select(self.driver.find_element(By.XPATH, CONF.readConfig("Locators", syntex))).select_by_value(1)


    def mousehover(self, syntex):
        configLoader = CONF.readConfig("Locators", syntex)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, configLoader)).perform()
