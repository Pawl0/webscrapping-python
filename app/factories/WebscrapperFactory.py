import sys
sys.path.append('./app/helpers')
sys.path.append('./app/epic')
sys.path.append('./app/kabum')
sys.path.append('./app/prime_game')
from epic import EpicWebscrapper
from kabum import KabumWebscrapper
from prime_game import PrimeWebscrapper

class WebscrapperFactory:
       
    _webscrappersList = {
        "epic": EpicWebscrapper,
        "kabum": KabumWebscrapper,
        "prime": PrimeWebscrapper,
    }
    def __init__(self, driverManager):
        self.driverManager = driverManager

    def makeWebscrapper(self, option):
        return self._webscrappersList[option](self.driverManager)