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
        itens = []
        for elementIndex in range(self.totalItemsToScrappe):
            elementsXpaths = self.getElementsXpathByIndex(elementIndex)
            for key in elementsXpaths:
                elementXpath = self.getElementByXpath(elementsXpaths[key])
                elementValue = elementXpath.get_attribute('innerHTML')
                print(elementValue)
                itens.append({
                    key: elementValue.replace('&nbsp;', ' '),
                })
        return itens

    @abstractmethod
    def getElementByXpath(self, xpath):
        pass

    def setUrl(self, url):
        self.url = url

    def getUrl(self):
        return self.url
