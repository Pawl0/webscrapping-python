import sys
sys.path.append('./app/helpers')
sys.path.append('./app/epic')
sys.path.append('./app/kabum')
sys.path.append('./app/prime_game')
sys.path.append('./app/indiegala')
sys.path.append('./app/epic_v')
from epic import EpicWebscrapper
from kabum import KabumWebscrapper
from prime_game import PrimeWebscrapper
from indiegala import IndieGalaWebscrapper
from epic_v import EpicVWebscrapper
from Webscrapper import Webscrapper
from SeleniumWebscrappingStrategy import SeleniumWebscrappingStrategy

class WebscrapperFactory:
    
    _webscrappersList = {
        "epic": EpicWebscrapper,
        "kabum": KabumWebscrapper,
        "prime": PrimeWebscrapper,
        "indiegala": IndieGalaWebscrapper,
        "epicV": EpicVWebscrapper,
    }
    def __init__(self, driverManager):
        self.driverManager = driverManager

    def makeWebscrapper(self, option) -> Webscrapper:
        return self._webscrappersList[option](SeleniumWebscrappingStrategy())