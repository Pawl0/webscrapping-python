from abc import ABC, abstractmethod

class Webscrapper(ABC):

    def __init__(self, driverManager):
        self.driverManager = driverManager

    @abstractmethod
    def getItensData():
        pass

    @abstractmethod
    def execute():
        pass