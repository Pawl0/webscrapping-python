from selenium.webdriver.common.keys import Keys
import time
from WebscrappingStrategy import WebscrappingStrategy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from helpers import DriverManager
import sys
sys.path.append('../helpers')


class SeleniumWebscrappingStrategy(WebscrappingStrategy):

    def __init__(self):
        self.driverManager = DriverManager()

    def getDriver(self):
        return self.driver

    def setupInternals(self):
        self.driver = self.driverManager.setupDriver(self.getUrl())
        time.sleep(6)
        self.scrollToBottom()

    def hook(self):
        self.driverManager.quit()

    def getElement(self, element):
        return element

    def pageUp(self):
        body = self.driver.find_element_by_xpath('/html/body')
        time.sleep(8)
        body.send_keys(Keys.PAGE_UP)

    def scrollToBottom(self):
        body = self.driver.find_element_by_xpath('/html/body')
        body.send_keys(Keys.END)

    def clickOnBody(self):
        body = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/div/div/div[3]/div[1]/div[1]/div/div[3]/button/div/p')
        body.click()

    def getInnerHTMLByXpath(self, xpath):
        element= self.driver.find_element(By.XPATH, xpath)
        return element.get_attribute('innerHTML')

    def getItensDecorated(self):
        try:
            return self.getItensData()
        except NoSuchElementException:
            print("Element not found")
            self.driverManager.quit()
            return self.getItens()
        except WebDriverException:
            print("WebDriver exception")
            self.driverManager.quit()
            return [] 
        except TimeoutException:
            print("Timeout exception")
            self.driverManager.quit()
            return [] 
        except:
            print("Unknown exception")
            self.driverManager.quit()
            return []