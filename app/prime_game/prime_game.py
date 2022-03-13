import sys
sys.path.append('../helpers')
from Webscrapper import Webscrapper
from SeleniumWebscrappingStrategy import SeleniumWebscrappingStrategy
from selenium.common.exceptions import NoSuchElementException
class PrimeWebscrapper(Webscrapper):

    url = "https://gaming.amazon.com/home"
    _filename = "amazon-prime-free-games"
    total_elements_to_scrappe = 7

    def __init__(self, webscrappingStrategy):
        self.seleniumStrategy = SeleniumWebscrappingStrategy()
        super().__init__(self.seleniumStrategy)

    def getItensData(self):
        try:
            return self.webscrappingStrategy.getItensData()
        except NoSuchElementException:
            print("Element not found")
            return self.seleniumStrategy.getItens()

    def getElementsXpathByIndex(self, elementIndex):
        elementDescription = self.getElementByIndex(elementIndex)
        return {
            "item": elementDescription
        }

    def getElementByIndex(self, elementIndex):
        driver = self.seleniumStrategy.getDriver()
        xpathPrefix = f'/html/body/div[1]/div/div[1]/main/div/div[2]/div/div[3]/div[5]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[{elementIndex + 1}]'
        try:
            xpath = xpathPrefix+'/div/div/div/a/div/div/div[2]/div/div[1]/h3'
            if (driver.find_element_by_xpath(xpath)):
                return xpath
        except:
            xpath = xpathPrefix+'/div/div/div/div/div/div[2]/div/div[1]/h3'
            return xpath