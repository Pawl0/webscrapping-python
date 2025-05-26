import sys
sys.path.append('./app/helpers')
sys.path.append('../helpers')
from Webscrapper import Webscrapper

class IndieGalaWebscrapper(Webscrapper):

    url = "https://freebies.indiegala.com/"
    _filename = "indiegala"
    total_elements_to_scrappe = 3
    name = "indiegala"

    def __init__(self, webscrappingStrategy):
        self.webscrappingStrategy = webscrappingStrategy
        super().__init__(self.webscrappingStrategy)

    def getElementsXpathByIndex(self, elementIndex):
        return {
            "item": self.webscrappingStrategy.getInnerHTMLByXpath(f"/html/body/div[1]/div/section/div[2]/div[3]/div[{elementIndex+1}]/div/figcaption/div[1]")
        }
