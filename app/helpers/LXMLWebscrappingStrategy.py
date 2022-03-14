from WebscrappingStrategy import WebscrappingStrategy
from helpers import DriverManager
import requests
from lxml import html
import sys
sys.path.append('../helpers')

class LXMLWebscrappingStrategy(WebscrappingStrategy):

    def setupInternals(self):
        header = {
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
            'AppleWebKit/537.11 (KHTML, like Gecko) '
            'Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }
        response = requests.get(self.url, headers=header)
        print(response)
        self.tree = html.fromstring(response.content)
        print(self.tree)

    def getElement(self, xpath):
        return str(self.tree.xpath(xpath+"/text()"))

    def getItensDecorated(self):
        return self.getItensData()
