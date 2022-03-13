from WebscrappingStrategy import WebscrappingStrategy
from helpers import DriverManager
import requests
from lxml import html
import sys
sys.path.append('../helpers')


class LXMLWebscrappingStrategy(WebscrappingStrategy):

    def setupInternals(self):
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        response = requests.get(self.url, headers=header)
        self.tree = html.fromstring(response.content)

    def getElementByXpath(self, xpath):
        return str(self.tree.xpath(xpath+"/text()"))
