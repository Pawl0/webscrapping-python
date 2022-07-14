import sys
sys.path.append('../helpers')
from Webscrapper import Webscrapper
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PrimeWebscrapper(Webscrapper):

    url = "https://gaming.amazon.com/home"
    _filename = "amazon-prime-free-games"
    total_elements_to_scrappe = 30
    name = "prime_game"

    def __init__(self, webscrappingStrategy):
        self.webscrappingStrategy = webscrappingStrategy
        super().__init__(self.webscrappingStrategy)
        self.webscrappingStrategy.clickOnBody()
        self.webscrappingStrategy.scrollToBottom()

    def getItensData(self):
        return self.webscrappingStrategy.getItensDecorated()

    def getElementsXpathByIndex(self, elementIndex):
        elementDescription = self.getInnerHTMLByIndex(elementIndex)
        return {
            "item": elementDescription
        }

    def getInnerHTMLByIndex(self, elementIndex):
        xpathPrefix = f'/html/body/div[1]/div/div[1]/main/div/div/div/div[4]/div[5]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[{elementIndex + 1}]/div/div/div'
        elementPrefix = self.webscrappingStrategy.getDriver().find_element(By.XPATH, xpathPrefix)
        elements = elementPrefix.find_elements_by_tag_name('p')
        element = elements[-2]
        self.webscrappingStrategy.pageUp()
        return element.get_attribute('innerHTML')