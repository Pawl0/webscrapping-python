from abc import ABC, abstractmethod
from helpers import saveJsonFile
from datetime import datetime

class Webscrapper(ABC):

    def __init__(self, webscrappingStrategy):
        self.webscrappingStrategy = webscrappingStrategy
        self.setupWebscrapper()
        self.setTotalElementsToScrappe(self.total_elements_to_scrappe)

    def setupWebscrapper(self):
        self.webscrappingStrategy.setupWebscrapper(self.url,
            self.getTotalElementsToScrappe(), self.getElementsXpathByIndex)

    def getItensData(self):
        return self.webscrappingStrategy.getItensDecorated()

    def setTotalElementsToScrappe(self, total_elements_to_scrappe):
        self.total_elements_to_scrappe = total_elements_to_scrappe

    def getTotalElementsToScrappe(self):
        return self.total_elements_to_scrappe

    def getElementXpathByIndex(self, elementIndex):
        pass

    def setWebscrappingStrategy(self, webscrappingStrategy):
        self.webscrappingStrategy = webscrappingStrategy

    def execute(self):
        items = self.getItensData()
        result = {
            "items": items,
            "last_run": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        }
        print(result)
        saveJsonFile(self._filename, result)
        return result
