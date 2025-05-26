import sys
sys.path.append('./app/helpers')
sys.path.append('../helpers')
from Webscrapper import Webscrapper

class EpicVWebscrapper(Webscrapper):

    url = "https://epic-virtual-boost.itch.io/"
    _filename = "epic-v"
    total_elements_to_scrappe = 3
    name = "epic_v"
    
    def getElementsXpathByIndex(self, elementIndex):
        return {
            "item": f"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[{elementIndex+1}]/div/div[1]/a[1]"
        }
