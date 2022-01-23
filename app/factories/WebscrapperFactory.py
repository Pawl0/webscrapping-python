import sys
sys.path.append('./app/epic')
sys.path.append('./app/kabum')
sys.path.append('./app/prime_game')
from epic import EpicWebscrapper
from kabum import KabumWebscrapper
from prime_game import PrimeWebscrapper

makeWebscrapper = {
    "epic": EpicWebscrapper,
    "kabum": KabumWebscrapper,
    "prime": PrimeWebscrapper,
}