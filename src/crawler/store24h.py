from .crawler import Crawler 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json 
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from tqdm import tqdm
import datetime
import os

class Store24h(Crawler):
    def __init__(self, source):
        super().__init__(source)
        #print(self.source)
        self.data = []
        self.filename = datetime.date.today().strftime(self.source+"%Y%m%d.json")

    def crawl(self):
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        categories = {'iphone': 'https://24hstore.vn/dien-thoai-iphone-apple'}
        urls = []

        for link in categories:
            driver.get(categories[link])
            flag = True
            for i in range(5):
                #print(i)
                try:
                    button = driver.find_element(By.XPATH, '//*[@id="load_more_button"]')
                    button.click()
                    time.sleep(1)
                except Exception as e:
                    continue

            urls = driver.find_elements(By.XPATH, '//div[@class="frame_inner"]/a')
            urls = [url.get_attribute('href') for url in urls]

            for url in tqdm(urls):
                try:
                    driver.get(url)
                    p_elms = driver.find_elements(By.XPATH, '//div[@class="list_same"]/a/span[2]')
                    r_elms = driver.find_elements(By.XPATH, '//span[@class="nick_name"]/span')
                    c_elms = driver.find_elements(By.XPATH, '//span[@class="lo_text"]')
                    prices = [elm.get_attribute('innerHTML') for elm in p_elms]
                    roms = [elm.get_attribute('innerHTML') for elm in r_elms]
                    colors = [elm.get_attribute('innerHTML') for elm in c_elms]
                    name = driver.find_element(By.XPATH, '//h1[@class="pull-left"]').get_attribute('innerHTML')

                    for i in range(len(colors)):
                        for j in range(len(roms)):
                            product = {}
                            product['name'] = name
                            product['rom'] = roms[j]
                            product['ram'] = 'unknown'
                            product['link'] = url
                            product['price'] = prices[j]
                            product['color'] = colors[i]
                            self.data.append(product)
                except Exception as e:
                    print(e)
                    continue
        driver.quit()


    def saveDataToLocalFile(self):
        path = os.path.join(os.getcwd(), 'data/', self.source, self.filename)
        with open(path, 'w') as f:
            f.write(json.dumps(self.data))
            f.close()
