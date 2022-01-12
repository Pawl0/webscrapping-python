from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import pandas as pd
import matplotlib.pyplot as plt

PAGE_LOAD_WAIT_TIME = 30

def setupDriver(url):
    option = Options()
    option.headless = True
    print("Opening driver...")
    driver = webdriver.Firefox(options=option)

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


def plotChart(itens):
    print("Plotting chart....")
    data = pd.DataFrame(itens)
    print(data.head(10))
    plotdata = data.head(10)
    plotdata.plot(kind='bar', x='item', y='price', color='red')
    plt.xticks(fontsize=6, rotation=0)
    plt.title("Top 10 Kabum")
    plt.show()
