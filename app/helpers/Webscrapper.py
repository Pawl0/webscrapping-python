from abc import ABC, abstractmethod
from helpers import saveJsonFile

class Webscrapper(ABC):
    
    def __init__(self, driverManager):
        self.driverManager = driverManager

    @abstractmethod
    def getItensData(self):
        pass

    def execute(self):
        self.driver = self.driverManager.setupDriver(self._url)
        itens = self.getItensData()
        print(itens)
        saveJsonFile(self._filename, itens)

        return itens