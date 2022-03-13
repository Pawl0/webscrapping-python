from abc import ABC, abstractmethod

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
            print(elementIndex)
            elementsXpaths = self.getElementsXpathByIndex(elementIndex)
            print(elementsXpaths)
            for key in elementsXpaths:
                print(key)
                print(elementsXpaths[key])
                elementValue = self.getElementByXpath(elementsXpaths[key])
                print(elementValue)
                self.itens.append({
                    key: elementValue.replace('&nbsp;', ' '),
                })
        self.hook()
        return self.itens
    
    def getItens(self):
        return self.itens

    def hook(self):
        pass

    @abstractmethod
    def getElementByXpath(self, xpath):
        pass

    def setUrl(self, url):
        self.url = url

    def getUrl(self):
        return self.url