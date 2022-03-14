from LXMLWebscrappingStrategy import LXMLWebscrappingStrategy
from SeleniumWebscrappingStrategy import SeleniumWebscrappingStrategy
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

class WebscrapperFactory:

    __webscrappersList = {
        "epic": {"scrapper": EpicWebscrapper, "strategy": SeleniumWebscrappingStrategy},
        "kabum": {"scrapper": KabumWebscrapper, "strategy": SeleniumWebscrappingStrategy},
        "prime": {"scrapper": PrimeWebscrapper, "strategy": SeleniumWebscrappingStrategy},
        "indiegala": {"scrapper": IndieGalaWebscrapper, "strategy": SeleniumWebscrappingStrategy},
        "epicV": {"scrapper": EpicVWebscrapper, "strategy": LXMLWebscrappingStrategy},
    }

    def makeWebscrapper(self, option):
        selectedWebscrapper = self.__webscrappersList[option]
        selectedStrategy = selectedWebscrapper["strategy"]
        return selectedWebscrapper["scrapper"](selectedStrategy())
