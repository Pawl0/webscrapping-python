from WebscrappingStrategy import WebscrappingStrategy
from helpers import DriverManager
import sys
sys.path.append('../helpers')


class SeleniumWebscrappingStrategy(WebscrappingStrategy):

    def setupInternals(self):
        self.driver = DriverManager().setupDriver(self.getUrl())

    def getElementByXpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)
