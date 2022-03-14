from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# We import this so we can specify the Firefox browser binary location
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re
import json
import os

PAGE_LOAD_WAIT_TIME = 30


class DriverManager:

    def __init__(self):
        self.open()

    def setupDriver(self, url):
        print("Getting data from: ", url)
        self.driver.get(url)
        print("Waiting page to load...")
        self.driver.implicitly_wait(PAGE_LOAD_WAIT_TIME)  # in seconds
        return self.driver

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def open(self):
        print("Opening driver...")
        if os.environ.get("FIREFOX_BIN") != None:
            FF_options = webdriver.FirefoxOptions()
            FF_profile = webdriver.FirefoxProfile()
            FF_options.headless = True
            FF_options.add_argument("-remote-debugging-port=9224")
            FF_options.log.level = "trace"
            FF_options.add_argument('--no-sandbox')
            FF_options.add_argument("--headless")
            FF_options.add_argument("--disable-gpu")
            FF_profile.update_preferences()
            binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))
            self.driver = webdriver.Firefox(options=FF_options, firefox_profile=FF_profile, executable_path=os.environ.get(
                'GECKODRIVER_PATH'), firefox_binary=binary)
        else:
            options = Options()
            options.headless = True
            self.driver = webdriver.Firefox(options=options)


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


def removeUselessCharsFromText(text):
    return text.replace('\\', ' ').replace('xa0', '').replace('&nbsp;', ' ').replace('[\'', '').replace('\']', '').replace('Grátis - ', '').replace('<time datetime="', '').replace('" data-component="Time">', ' ').replace('</time>', '')


def extractISODateFromText(text: str):
    return re.search(r'\d{4}-\d{2}-\d{2}T\d+:\d+:\d+.\d+Z', text).group(0)
