import sys
sys.path.append('./app/helpers')
sys.path.append('../helpers')
from Webscrapper import Webscrapper
from helpers import DriverManager


class IndieGalaWebscrapper(Webscrapper):

    _url = "https://freebies.indiegala.com/"
    _filename = "indiegala"

    def getItensData(self):
        itens = []
        for elementIndex in range(3):
            elementDescription = self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div/section/div[2]/div[3]/div[{elementIndex+1}]/div/figcaption/div[1]")

            description = elementDescription.get_attribute('innerHTML')

            print(description)

            itens.append({
                "item": description
            })
        return itens

if __name__ == "__main__":
    indiegalaWebscrapper = IndieGalaWebscrapper(DriverManager())
    indiegalaWebscrapper.execute()
