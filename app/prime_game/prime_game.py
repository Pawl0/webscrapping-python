import sys
sys.path.append('../helpers')
from Webscrapper import Webscrapper
from SeleniumWebscrappingStrategy import SeleniumWebscrappingStrategy
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PrimeWebscrapper(Webscrapper):

    url = "https://gaming.amazon.com/home"
    _filename = "amazon-prime-free-games"
    total_elements_to_scrappe = 100

    def __init__(self, webscrappingStrategy):
        self.webscrappingStrategy = webscrappingStrategy
        super().__init__(self.webscrappingStrategy)
        self.webscrappingStrategy.clickOnBody()
        self.webscrappingStrategy.scrollToBottom()

    def getItensData(self):
        try:
            return self.webscrappingStrategy.getItensData()
        except NoSuchElementException:
            print("Element not found")
            return self.webscrappingStrategy.getItens()
        except WebDriverException:
            print("WebDriver exception")
            return [] 
        except TimeoutException:
            print("Timeout exception")
            return [] 
        except:
            print("Unknown exception")
            return []

    def getElementsXpathByIndex(self, elementIndex):
        elementDescription = self.getInnerHTMLByIndex(elementIndex)
        return {
            "item": elementDescription
        }

    def getInnerHTMLByIndex(self, elementIndex):
        xpathPrefix = f'/html/body/div[1]/div/div[1]/main/div/div[2]/div/div[3]/div[5]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[{elementIndex + 1}]/div/div/div'
        elementPrefix = self.webscrappingStrategy.getDriver().find_element(By.XPATH, xpathPrefix)
        element = elementPrefix.find_element_by_tag_name('h3')
        return element.get_attribute('innerHTML')