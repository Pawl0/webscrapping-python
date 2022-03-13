import sys
sys.path.append('../helpers')
from Webscrapper import Webscrapper

class KabumWebscrapper(Webscrapper):
    
    url = "https://www.kabum.com.br/"
    _filename = "kabum-top-10"
    total_elements_to_scrappe = 10

    def getElementsXpathByIndex(self, elementIndex):
        return {
            "item": f"/html/body/div/main/div/article/section[1]/div[1]/div[2]/div[1]/div/div/div/div[{elementIndex+1}]/div/div/a/div/div[1]/h2",
            "price": f"/html/body/div/main/div/article/section[1]/div[1]/div[2]/div[1]/div/div/div/div[{elementIndex+1}]/div/div/a/div/div[2]/span[2]"
        }