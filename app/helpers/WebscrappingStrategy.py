from abc import ABC, abstractmethod
from helpers import removeUselessCharsFromText
from helpers import extractISODateFromText

class WebscrappingStrategy(ABC):

    def setupWebscrapper(self, url, totalItemsToScrappe, getElementsXpathByIndex):
        self.setUrl(url)
        self.setupInternals()
        self.totalItemsToScrappe = totalItemsToScrappe
        self.getElementsXpathByIndex = getElementsXpathByIndex

    @abstractmethod
    def setupInternals(self):
        pass

    def getItensData(self):
        self.itens = []
        for elementIndex in range(self.totalItemsToScrappe):
            elementsXpaths = self.getElementsXpathByIndex(elementIndex)
            item = {}
            for key in elementsXpaths:
                elementValue = self.getElement(elementsXpaths[key])
                if (key == "until"):
                    item[key] = extractISODateFromText(elementValue)
                else:
                    item[key] = removeUselessCharsFromText(elementValue)
            self.itens.append(item)
        self.hook()
        return self.itens
    
    @abstractmethod
    def getItensDecorated(self):
        pass
        
    def getItens(self):
        return self.itens

    def hook(self):
        pass

    @abstractmethod
    def getElement(self, xpath):
        pass

    def setUrl(self, url):
        self.url = url

    def getUrl(self):
        return self.url