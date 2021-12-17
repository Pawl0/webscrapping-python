import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.kabum.com.br/"

option = Options()
option.headless = True
print("Opening driver")
driver = webdriver.Firefox(options=option)

print("Getting data from: ", url)
driver.get(url)
print("Waiting page to load...")
driver.implicitly_wait(30)  # in seconds

itens = []

try:
    print("Processing data....")
    for elementIndex in range(10):
        elementDescription = driver.find_element_by_xpath(
            f"//html//body//div//main//div//article//section[1]//div[1]//div[2]//div[1]//div//div//div//div[{elementIndex+1}]//div//div//a//div//div[1]//h2")
        elementPrice = driver.find_element_by_xpath(
            f"//html//body//div//main//div//article//section[1]//div[1]//div[2]//div[1]//div//div//div//div[{elementIndex+1}]//div//div//a//div//div[2]//span[2]")

        description = elementDescription.get_attribute('innerHTML')
        html_price = elementPrice.get_attribute('innerHTML')

        price = html_price.replace('&nbsp;', ' ')

        print(description)
        print(price)

        itens.append({
            "item": description.replace(' ', '\n'),
            "price": float(price[3:].replace(".", "").replace(",", "."))
        })

    driver.quit()

    print(itens)

    print("Plotting chart....")
    data = pd.DataFrame(itens)
    print(data.head(10))
    plotdata = data.head(10)
    plotdata.plot(kind='bar', x='item', y='price', color='red')
    plt.xticks(fontsize=6, rotation=0)
    plt.title("Top 10 Kabum")
    plt.show()

    print("Saving file as json....")
    with open('kabum-top-10.json', 'w', encoding='utf-8') as jp:
        js = json.dumps(itens, indent=4)
        jp.write(js)

except error:
    print(error)
    driver.close()
    driver.quit()
