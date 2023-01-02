from .crawler import Crawler 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json 
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from tqdm import tqdm
import datetime
import os
import re

class Xtmobile(Crawler):
    def __init__(self, source):
        super().__init__(source)
        #print(self.source)
        self.data = []
        self.filename = datetime.date.today().strftime(self.source+"%Y%m%d.json")

    def crawl(self):
        data = []
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

        urls = []

        # for category in apple_categories:
        driver.get('https://www.xtmobile.vn/apple')
        x_path = '/html/body/div[6]/div/div[2]/div[2]/div/div/div[5]/form/a'
        try:
            for i in range(5):
                button = driver.find_element(By.XPATH, x_path)
                if button is None:
                    break
                button.click()
                time.sleep(2)
        except Exception as e:
            print(e)
            pass


        items = driver.find_element(By.ID,'List_Product').find_elements(By.CLASS_NAME, 'product-info-top')
        for item in items:
            urls.append(item.find_element(By.TAG_NAME,'a').get_attribute('href'))

        for url in tqdm(urls):
            driver.get(url)
            try:
                url_img = 'unknown'
                list_rom = driver.find_element(By.XPATH, '//*[@id="form_order"]/div[2]')
                list_rom_a = list_rom.find_elements(By.TAG_NAME, 'a')
                list_rom_url = [L.get_attribute('href') for L in list_rom_a]

                list_rom_span = list_rom.find_elements(By.TAG_NAME, 'span')
                list_rom_data = [L.get_attribute('innerHTML') for L in list_rom_span]  




                for id, i in enumerate(list_rom_url):
                    product = {}

                    rom = list_rom_data[id]
                    link = None
                    try:
                        if id == 0:
                            link = url
                        else:
                            link = list_rom_url[id]
                            driver.get(link)
                        if 'javascript' in link:
                            link = url
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
            except Exception as e:
                url_img = 'unknown'
                continue
        self.data = data
        driver.quit()
        return data

    def saveDataToLocalFile(self):
        path = os.path.join(os.getcwd(), 'data/', self.source, self.filename)
        with open(path, 'w') as f:
            f.write(json.dumps(self.data))
            f.close()
