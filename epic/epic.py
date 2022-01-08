from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json


def setupDriver(url):
    option = Options()
    option.headless = True
    print("Opening driver...")
    driver = webdriver.Firefox(options=option)

    print("Getting data from: ", url)
    driver.get(url)
    print("Waiting page to load...")
    # driver.implicitly_wait(10)  # in seconds
    return driver


def saveJsonFile(name, itens):
    print("Saving file as json....")
    with open(name+'.json', 'w', encoding='utf-8') as jp:
        js = json.dumps(itens, indent=4)
        jp.write(js)


def getItensData():
    itens = []
    elementDescription = driver.find_element_by_xpath(
        f'//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[1]/div/div/a/div/div/div[3]/span[1]/div')
    elementPeriod = driver.find_element_by_xpath(
        f'//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[1]/div/div/a/div/div/div[3]/span[2]/div')

    description = elementDescription.get_attribute('innerHTML')
    time = elementPeriod.find_element_by_tag_name(
        'time').get_attribute('innerHTML')

    print(description)
    print(time)

    itens.append({
        "item": description,
        "until": time,
    })
    return itens


try:
    driver = setupDriver("https://www.epicgames.com/store/pt-BR/")

    itens = getItensData()

    driver.quit()

    print(itens)

    saveJsonFile("epic free games", itens)

except error:
    print(error)
    driver.close()
    driver.quit()
