import sys
sys.path.append('../helpers')
from Webscrapper import Webscrapper

class PrimeWebscrapper(Webscrapper):

    url = "https://gaming.amazon.com/home"
    _filename = "amazon-prime-free-games"
    total_elements_to_scrappe = 9

    def getItensData(self):
        try:
            return self.webscrapperAdapter.getItensData()
        except:
            return []

    def getElementsXpathByIndex(self, elementIndex):
        return {
            "item": f'/ html/body/div[1]/div/div[1]/main/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[{elementIndex}]'
        }

    # def getItensData(self):
    #     itens = []
    #     try:
    #         elementIndex = 1
    #         element = self.getElementByIndex(elementIndex)
    #         while (element and elementIndex < 9):
    #             elementDescription = element.find_element_by_tag_name('h3')
    #             description = elementDescription.get_attribute('innerHTML')
    #             time = element.find_element_by_tag_name(
    #                 'span').get_attribute('innerHTML')

    #             print(description)
    #             print(time)

    #             itens.append({
    #                 "item": description,
    #                 "until": time,
    #             })
    #             elementIndex += 1
    #             element = self.getElementByIndex(elementIndex)
    #         return itens
    #     except:
    #         return itens