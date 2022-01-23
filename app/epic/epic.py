import os
import sys
sys.path.append('../helpers')
from helpers import saveJsonFile, DriverManager
from Webscrapper import Webscrapper

class EpicWebscrapper(Webscrapper):

    def getItensData(self):
        itens = []
        elementDescription = self.driver.find_element_by_xpath(
            f'//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[1]/div/div/a/div/div/div[3]/span[1]/div')
        elementPeriod = self.driver.find_element_by_xpath(
            f'//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[1]/div/div/a/div/div/div[3]/span[2]/div')

        description = elementDescription.get_attribute('innerHTML')
        time = elementPeriod.find_element_by_tag_name(
            'time').get_attribute('innerHTML')

        print(description)
        print(time)

        itens.append({
            "item": description,
            "until": time,
        })
        return itens

    def execute(self):
        self.driver = self.driverManager.setupDriver("https://www.epicgames.com/store/pt-BR/")
        itens = self.getItensData()
        print(itens)
        saveJsonFile("epic-free-games", itens)

        return itens

if __name__ == "__main__":
    epicWebscrapper = EpicWebscrapper()
    epicWebscrapper.execute()