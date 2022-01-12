import sys
sys.path.append('../helpers')
from helpers import saveJsonFile, setupDriver

def getItensData(driver):
    itens = []
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
            "item": description,
            # "item": description.replace(' ', '\n'),
            "price": float(price[3:].replace(".", "").replace(",", "."))
        })
    return itens

def main():
    try:
        driver = setupDriver("https://www.kabum.com.br/")

        itens = getItensData(driver)

        print(itens)

        # plotChart(itens)
        saveJsonFile('kabum-top-10', itens)

        return itens
    except:
        print("An error has ocurred")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()