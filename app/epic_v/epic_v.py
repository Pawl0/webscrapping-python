import sys
sys.path.append('./app/helpers')
sys.path.append('../helpers')
from Webscrapper import Webscrapper
from helpers import DriverManager


class EpicVWebscrapper(Webscrapper):

    _url = "https://epic-virtual-boost.itch.io/"
    _filename = "epic-v"

    def getItensData(self):
        itens = []
        for elementIndex in range(4):
            elementDescription = self.driver.find_element_by_xpath(
                f"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[{elementIndex+1}]/div/div[1]/a[1]")

            description = elementDescription.get_attribute('innerHTML')

            print(description)

            itens.append({
                "item": description
            })
        return itens

if __name__ == "__main__":
    epicVWebscrapper = EpicVWebscrapper(DriverManager())
    epicVWebscrapper.execute()
