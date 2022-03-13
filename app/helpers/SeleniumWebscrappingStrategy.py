from WebscrappingStrategy import WebscrappingStrategy
from helpers import DriverManager
import sys
sys.path.append('../helpers')
import time
from selenium.webdriver.common.keys import Keys

class SeleniumWebscrappingStrategy(WebscrappingStrategy):

    def __init__(self):
        self.driverManager = DriverManager()

    def getDriver(self):
        return self.driver

    def setupInternals(self):
        self.driver = self.driverManager.setupDriver(self.getUrl())  
        time.sleep(3)
        self.driver.find_element_by_tag_name('body').click()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)

    def hook(self):
        self.driverManager.close()

    def getElementByXpath(self, xpath):
        elementXpath = self.driver.find_element_by_xpath(xpath)
        return elementXpath.get_attribute('innerHTML')