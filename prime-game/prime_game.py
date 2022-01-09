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
    driver.implicitly_wait(20)  # in seconds
    return driver


def saveJsonFile(name, itens):
    print("Saving file as json....")
    with open(name+'.json', 'w', encoding='utf-8') as jp:
        js = json.dumps(itens, indent=4)
        jp.write(js)


def getElementByIndex(index):
    return driver.find_element_by_xpath(
        f'/ html/body/div[1]/div/div[1]/main/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[{index}]')


def getItensData():
    itens = []
    try:
        elementIndex = 1
        element = getElementByIndex(elementIndex)

        while (element):
            elementDescription = element.find_element_by_tag_name('h3')

            description = elementDescription.get_attribute('innerHTML')
            time = element.find_element_by_tag_name(
                'span').get_attribute('innerHTML')

            print(description)
            print(time)

            itens.append({
                "item": description,
                "until": time,
            })
            elementIndex += 1
            element = getElementByIndex(elementIndex)
    except:
        return itens


try:
    driver = setupDriver("https://gaming.amazon.com/home")

    itens = getItensData()

    driver.close()
    driver.quit()

    print(itens)

    saveJsonFile("amazon prime free games", itens)

except error:
    print(error)
    driver.close()
    driver.quit()
