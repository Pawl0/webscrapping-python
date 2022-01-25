import sys
sys.path.append('./app/helpers')
sys.path.append('./app/epic')
sys.path.append('./app/kabum')
sys.path.append('./app/prime_game')
sys.path.append('./app/indiegala')
from epic import EpicWebscrapper
from kabum import KabumWebscrapper
from prime_game import PrimeWebscrapper
from indiegala import IndieGalaWebscrapper

class WebscrapperFactory:
       
    _webscrappersList = {
        "epic": EpicWebscrapper,
        "kabum": KabumWebscrapper,
        "prime": PrimeWebscrapper,
        "indiegala": IndieGalaWebscrapper,
    }
    def __init__(self, driverManager):
        self.driverManager = driverManager

    def makeWebscrapper(self, option):
        return self._webscrappersList[option](self.driverManager)