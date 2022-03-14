from selenium.webdriver.common.keys import Keys
import time
from WebscrappingStrategy import WebscrappingStrategy
from helpers import DriverManager
import sys
sys.path.append('../helpers')


class SeleniumWebscrappingStrategy(WebscrappingStrategy):

    def __init__(self):
        self.driverManager = DriverManager()

    def getDriver(self):
        return self.driver

    def setupInternals(self):
        self.driver = self.driverManager.setupDriver(self.getUrl())
        time.sleep(2)
        self.scrollToBottom()

    def hook(self):
        self.driverManager.quit()

    def getElement(self, element):
        return element

    def scrollToBottom(self):
        body = self.driver.find_element_by_xpath('/html/body')
        body.send_keys(Keys.END)

    def clickOnBody(self):
        body = self.driver.find_element_by_xpath('/html/body')
        body.click()
