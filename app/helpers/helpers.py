from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import os

PAGE_LOAD_WAIT_TIME = 30

def setupDriver(url):
    options = Options()
    options.headless = True
    options.binary_location = os.environ.get("FIREFOX_BIN")
    print("Opening driver...")
    driver = webdriver.Firefox(executable_path=os,environ.get("GECKODRIVER_PATH"), options=options)

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