from helpers import DriverManager
from abc import ABC, abstractmethod

class Webscrapper(ABC):

    def __init__(self):
        self.driverManager = DriverManager()

    @abstractmethod
    def getItensData():
        pass