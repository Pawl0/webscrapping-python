import sys
sys.path.append('../helpers')
from Webscrapper import Webscrapper

class KabumWebscrapper(Webscrapper):
    
    url = "https://www.kabum.com.br/"
    _filename = "kabum-top-10"
    total_elements_to_scrappe = 10
    name = "kabum"
    
    def __init__(self, webscrappingStrategy):
        self.webscrappingStrategy = webscrappingStrategy
        super().__init__(self.webscrappingStrategy)
        
    def getElementsXpathByIndex(self, elementIndex):
        return {
            "item": self.webscrappingStrategy.getInnerHTMLByXpath(f"//html//body//div[2]//main//div[1]//div[2]//div//div//div//div[1]//div//div//div[{18+elementIndex+1}]//div//div//a//div[1]//div[1]//h2//span"),
            "price": self.webscrappingStrategy.getInnerHTMLByXpath(f"//html//body//div[2]//main//div[1]//div[2]//div//div//div//div[1]//div//div//div[{18+elementIndex+1}]//div//div//a//div//div[2]//span[2]")
        }