import sys
sys.path.append('../helpers')
from helpers import DriverManager
from Webscrapper import Webscrapper

class KabumWebscrapper(Webscrapper):
    
    _url = "https://www.kabum.com.br/"
    _filename = "kabum-top-10"

    def getItensData(self):
        itens = []
        for elementIndex in range(10):
            elementDescription = self.driver.find_element_by_xpath(
                f"//html//body//div//main//div//article//section[1]//div[1]//div[2]//div[1]//div//div//div//div[{elementIndex+1}]//div//div//a//div//div[1]//h2")
            elementPrice = self.driver.find_element_by_xpath(
                f"//html//body//div//main//div//article//section[1]//div[1]//div[2]//div[1]//div//div//div//div[{elementIndex+1}]//div//div//a//div//div[2]//span[2]")

            description = elementDescription.get_attribute('innerHTML')
            html_price = elementPrice.get_attribute('innerHTML')

            price = html_price.replace('&nbsp;', ' ')

            print(description)
            print(price)

            itens.append({
                "item": description,
                # "item": description.replace(' ', '\n'),
                "price": float(price[3:].replace(".", "").replace(",", "."))
            })
        return itens

if __name__ == "__main__":
    kabumWebscrapper = KabumWebscrapper()
    kabumWebscrapper.execute()