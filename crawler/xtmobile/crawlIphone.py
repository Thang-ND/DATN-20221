from math import prod
import time
from attr import attrib
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from tqdm import tqdm
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from json import dumps
# import schedule
import time


def crawl():
    data = []
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    urls = []
    products = []
    apple_categories = {
        'iphone': 'https://www.xtmobile.vn/apple'
    }
    # for category in apple_categories:
    driver.get('https://www.xtmobile.vn/apple')
    x_path = '/html/body/div[6]/div/div[2]/div[2]/div/div/div[5]/form/a'
    for i in range(5):
        print("*")
        button = driver.find_element(By.XPATH, x_path)
        if button is None:
            break
        try:
            button.click()
        except:
            continue
        time.sleep(2)


    items = driver.find_element(By.ID,'List_Product').find_elements(By.CLASS_NAME, 'product-info-top')
    for item in items:
        urls.append(item.find_element(By.TAG_NAME,'a').get_attribute('href'))
    # urls.append('https://www.xtmobile.vn/iphone-14-pro-max-chinh-hang')
    for url in tqdm(urls):
        driver.get(url)
        try:
            url_img = driver.find_element(By.XPATH, '//*[@id="divInfo"]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/div[1]/div/img').get_attribute('src')
            list_rom = driver.find_element(By.XPATH, '//*[@id="form_order"]/div[2]')
            list_rom_a = list_rom.find_elements(By.TAG_NAME, 'a')
            list_rom_url = [L.get_attribute('href') for L in list_rom_a]

            list_rom_span = list_rom.find_elements(By.TAG_NAME, 'span')
            list_rom_data = [L.get_attribute('innerHTML') for L in list_rom_span]  
        except Exception as e:
            url_img = 'unknown'
            pass

        # print(list_rom_url)
        # print(list_rom_data)


        for id, i in enumerate(list_rom_url):
            product = {}
            print(i)
            rom = list_rom_data[id]
            link = None
            try:
                if id == 0:
                    link = url
                else:
                    link = list_rom_url[id]
                    driver.get(link)
                list_color = driver.find_element(By.CLASS_NAME, 'color-list-show')
                # a_element = list_color.find_elements(By.TAG_NAME, 'a')
                p_color_elements = list_color.find_elements(By.TAG_NAME, 'p')
                price_elements = list_color.find_elements(By.CLASS_NAME, 'price')
                colors = [P.get_attribute('innerHTML') for P in p_color_elements]
                prices = [P.get_attribute('innerHTML') for P in price_elements]
                # print(colors)
                # print(prices)
                name = driver.find_element(By.CLASS_NAME, 'name-sp').get_attribute('innerHTML')
            except Exception as e:
                continue

            for index in range(len(colors)):
                tmp = {}
                tmp['color'] = colors[index]
                tmp['price'] = prices[index]
                tmp['url'] = link
                tmp['name'] = name
                tmp['rom'] = rom
                tmp['url_img'] = url_img
                data.append(tmp)

    return data
if __name__ == '__main__':
    print("start")
    data = crawl()
    with open('./data.json', 'w') as f:
        f.write(json.dumps(data))
        f.close
    # print("end")
    # print(len(data))
    # # print(urls)
