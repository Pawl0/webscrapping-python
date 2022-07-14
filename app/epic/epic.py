import sys
sys.path.append('../helpers')
from Webscrapper import Webscrapper

class EpicWebscrapper(Webscrapper):

    url = "https://www.epicgames.com/store/pt-BR/"
    _filename = "epic-free-games"
    total_elements_to_scrappe = 2
    name = "epic"
    
    def __init__(self, webscrappingStrategy):
        self.webscrappingStrategy = webscrappingStrategy
        super().__init__(self.webscrappingStrategy)

    def getElementsXpathByIndex(self, elementIndex):
        return {
            "item": self.webscrappingStrategy.getInnerHTMLByXpath(f'//html//body//div[1]//div//div[4]//main//div[2]//div//div//div//span[4]//div//div//section//div//div[{elementIndex+1}]//div//div//a//div//div//div[3]//span[1]//div'),
            "until": self.webscrappingStrategy.getInnerHTMLByXpath(f'//html//body//div[1]//div//div[4]//main//div[2]//div//div//div//span[4]//div//div//section//div//div[{elementIndex+1}]//div//div//a//div//div//div[3]//span[2]//div//span')
        }
