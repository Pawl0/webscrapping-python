import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://www.kabum.com.br/"

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)
driver.implicitly_wait(30)  # in seconds

itens = []

for elementIndex in range(10):
    element = driver.find_element_by_xpath(
        f"//html//body//div[1]//main//div[1]//article//section[1]//div[1]//div[2]//div[1]//div//div//div//div[{elementIndex+1}]//div//div//div//a//h2")
    elementPrice = driver.find_element_by_xpath(
        f"//html//body//div[1]//main//div[1]//article//section[1]//div[1]//div[2]//div[1]//div//div//div//div[{elementIndex+1}]//div//div//div//a//div//span[2]")
    html_content = element.get_attribute('innerHTML')
    html_price = elementPrice.get_attribute('innerHTML')

    price = html_price.replace('&nbsp;', ' ')

    itens.insert(elementIndex, {
        "item": html_content,
        "price": price
    })

driver.quit()

print(itens)

with open('kabum-top-10.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(itens, indent=4)
    jp.write(js)