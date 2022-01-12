import sys
sys.path.append('../helpers')
from helpers import saveJsonFile, setupDriver


def getElementByIndex(driver, index):
    return driver.find_element_by_xpath(
        f'/ html/body/div[1]/div/div[1]/main/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[{index}]')


def getItensData(driver):
    itens = []
    try:
        elementIndex = 1
        element = getElementByIndex(driver, elementIndex)
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
            element = getElementByIndex(driver, elementIndex)
    except:
        return itens

def main():
    # try:
        driver = setupDriver("https://gaming.amazon.com/home")

        itens = getItensData(driver)

        print(itens)

        saveJsonFile("amazon-prime-free-games", itens)

        return itens
    # except:
    #     print("An error has ocurred")
    # finally:
    #     driver.quit()

if __name__ == "__main__":
    main()