from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary #We import this so we can specify the Firefox browser binary location

import json
import os

PAGE_LOAD_WAIT_TIME = 20
print("Opening driver...")

class DriverManager:

    def __init__(self):
        if os.environ.get("FIREFOX_BIN") != None:
            FF_options = webdriver.FirefoxOptions()
            FF_profile = webdriver.FirefoxProfile()
            FF_options.add_argument("-headless")
            FF_profile.update_preferences()
            self.driver = webdriver.Firefox(options=FF_options, firefox_profile=FF_profile, executable_path=os.environ.get("GECKODRIVER_PATH"), firefox_binary=FirefoxBinary(os.environ.get("FIREFOX_BIN")))
        else:
            options = Options()
            options.headless = True
            self.driver = webdriver.Firefox(options=options)

    def setupDriver(self, url):
        print("Getting data from: ", url)
        self.driver.get(url)
        print("Waiting page to load...")
        self.driver.implicitly_wait(PAGE_LOAD_WAIT_TIME)  # in seconds
        return self.driver


def saveJsonFile(name, itens):
    print("Saving file as json....")
    filename = name+'.json'
    with open(filename, 'w', encoding='utf-8') as jp:
        js = json.dumps(itens, indent=4)
        jp.write(js)
        print('File saved as: ', filename)

def openJsonFile(name):
    file = open(name)
    data = json.load(file)
    return data