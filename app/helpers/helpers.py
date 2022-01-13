from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary #We import this so we can specify the Firefox browser binary location

import json
import os

PAGE_LOAD_WAIT_TIME = 20
FF_options = webdriver.FirefoxOptions()
FF_profile = webdriver.FirefoxProfile()
FF_options.add_argument("-headless")
FF_profile.update_preferences()
print("Opening driver...")
driver = webdriver.Firefox(options=FF_options, firefox_profile=FF_profile, executable_path=os.environ.get("GECKODRIVER_PATH"), firefox_binary=FirefoxBinary(os.environ.get("FIREFOX_BIN")))

def setupDriver(url):
    # options = Options()
    # options.headless = True
    # options.binary_location = os.environ.get("FIREFOX_BIN")
    
    # driver = webdriver.Firefox(executable_path=os,environ.get("GECKODRIVER_PATH"), options=options)
    print("Getting data from: ", url)
    driver.get(url)
    print("Waiting page to load...")
    driver.implicitly_wait(PAGE_LOAD_WAIT_TIME)  # in seconds
    return driver


def saveJsonFile(name, itens):
    print("Saving file as json....")
    filename = name+'.json'
    with open(filename, 'w', encoding='utf-8') as jp:
        js = json.dumps(itens, indent=4)
        jp.write(js)
        print('File saved as: ', filename)

def openJsonFile(name):
    f = open(name)
    data = json.load(file)
    return data