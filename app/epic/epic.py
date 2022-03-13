import sys
sys.path.append('../helpers')
from Webscrapper import Webscrapper
from SeleniumWebscrappingStrategy import SeleniumWebscrappingStrategy

class EpicWebscrapper(Webscrapper):

    url = "https://www.epicgames.com/store/pt-BR/"
    _filename = "epic-free-games"
    total_elements_to_scrappe = 1

    # def getItensData(self):
    #     itens = []
    #     elementDescription = self.driver.find_element_by_xpath(
    #         f'//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[1]/div/div/a/div/div/div[3]/span[1]/div')
    #     elementPeriod = self.driver.find_element_by_xpath(
    #         f'//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[1]/div/div/a/div/div/div[3]/span[2]/div')

    #     description = elementDescription.get_attribute('innerHTML')
    #     time = elementPeriod.find_element_by_tag_name(
    #         'time').get_attribute('innerHTML')

    #     print(description)
    #     print(time)

    #     itens.append({
    #         "item": description,
    #         "until": time,
    #     })
    #     return itens

    def __init__(self, webscrappingStrategy):
        super().__init__(SeleniumWebscrappingStrategy())

    def getElementsXpathByIndex(self, elementIndex):
        return {
            "item": f'//html//body//div[1]//div//div[4]//main//div[2]//div//div//div//span[5]//div//div//section//div//div[1]//div//div//a//div//div//div[3]//span[1]//div',
            "until": f'//html//body//div[1]//div//div[4]//main//div[2]//div//div//div//span[5]//div//div//section//div//div[1]//div//div//a//div//div//div[3]//span[2]//div//span'
        }
