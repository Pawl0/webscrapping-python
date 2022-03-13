from WebscrappingStrategy import WebscrappingStrategy
from helpers import DriverManager
import requests
from lxml import html
import sys
sys.path.append('../helpers')


class LXMLWebscrappingStrategy(WebscrappingStrategy):

    def setupInternals(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
        }
        response = requests.get(self.url, headers=header)
        print(response)
        self.tree = html.fromstring(response.content)
        print(self.tree)

    def getElementByXpath(self, xpath):
        print(xpath)
        return str(self.tree.xpath(xpath+"/text()"))
