import sys
sys.path.append('./app/helpers')
sys.path.append('../helpers')
from Webscrapper import Webscrapper
from SeleniumWebscrappingStrategy import SeleniumWebscrappingStrategy
from selenium.webdriver.common.by import By

class IndieGalaWebscrapper(Webscrapper):

    url = "https://freebies.indiegala.com/"
    _filename = "indiegala"
    total_elements_to_scrappe = 3

    def __init__(self, webscrappingStrategy):
        self.seleniumStrategy = SeleniumWebscrappingStrategy()
        super().__init__(self.seleniumStrategy)

    def getElementsXpathByIndex(self, elementIndex):
        return {
            "item": self.getInnerHTMLByXpath(f"/html/body/div[1]/div/section/div[2]/div[3]/div[{elementIndex+1}]/div/figcaption/div[1]")
        }
    
    def getInnerHTMLByXpath(self, xpath):
        element= self.seleniumStrategy.getDriver().find_element(By.XPATH, xpath)
        return element.get_attribute('innerHTML')
