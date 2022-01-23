import sys
sys.path.append('../helpers')
from helpers import saveJsonFile, DriverManager
from Webscrapper import Webscrapper

class PrimeWebscrapper(Webscrapper):

    def getElementByIndex(self, index):
        return self.driver.find_element_by_xpath(
            f'/ html/body/div[1]/div/div[1]/main/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[{index}]')

    def getItensData(self):
        itens = []
        try:
            elementIndex = 1
            element = self.getElementByIndex(elementIndex)
            while (element and elementIndex < 9):
                elementDescription = element.find_element_by_tag_name('h3')
                description = elementDescription.get_attribute('innerHTML')
                time = element.find_element_by_tag_name(
                    'span').get_attribute('innerHTML')

                print(description)
                print(time)

                itens.append({
                    "item": description,
                    "until": time,
                })
                elementIndex += 1
                element = self.getElementByIndex(elementIndex)
            return itens
        except:
            return itens

    def execute(self):
        self.driver = self.driverManager.setupDriver("https://gaming.amazon.com/home")
        itens = self.getItensData()
        print(itens)
        saveJsonFile("amazon-prime-free-games", itens)

        return itens

if __name__ == "__main__":
    primeWebscrapper = PrimeWebscrapper()
    primeWebscrapper.execute()