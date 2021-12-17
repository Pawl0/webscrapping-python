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
driver.implicitly_wait(20)  # in seconds

itens = []

try:
    for elementIndex in range(10):
        elementDescription = driver.find_element_by_xpath(
            f"//html//body//div//main//div//article//section[1]//div[1]//div[2]//div[1]//div//div//div//div[{elementIndex+1}]//div//div//a//div//div[1]//h2")
        elementPrice = driver.find_element_by_xpath(
            f"//html//body//div//main//div//article//section[1]//div[1]//div[2]//div[1]//div//div//div//div[{elementIndex+1}]//div//div//a//div//div[2]//span[2]")

        html_content = elementDescription.get_attribute('innerHTML')
        html_price = elementPrice.get_attribute('innerHTML')

        price = html_price.replace('&nbsp;', ' ')

        print(html_content)
        print(price)

        itens.append({
            "item": html_content,
            "price": price
        })

    driver.quit()

    print(itens)

    with open('kabum-top-10.json', 'w', encoding='utf-8') as jp:
        js = json.dumps(itens, indent=4)
        jp.write(js)

except error:
    print(error)
    driver.close()
    driver.quit()
