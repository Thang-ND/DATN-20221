from .crawler import Crawler 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json 
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from tqdm import tqdm
import datetime
import os

class Viettablet(Crawler):
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

        apple_categories = {
            'iphone': 'https://www.viettablet.com/iphone'
        }
        # for category in apple_categories:
        driver.get(apple_categories['iphone'])
        x_path = '//a[contains(@class, "more_load_page")]'
        try:
            for i in range(10):
                button = driver.find_element(By.XPATH, x_path)
                if button is None:
                    break
                button.click()
                time.sleep(2)
        except Exception as e:
            #print(e)
            pass


        items = driver.find_elements(By.XPATH,'//div[contains(@class, "product_list_column5")]/div/div[1]/a')
        urls = [item.get_attribute('href') for item in items]

        for url in tqdm(urls):
            driver.get(url)
            try:
                url_img = 'unknown'
                name = driver.find_element(By.XPATH, '//*[@id="thong_tin_san_pham"]/div/div[2]/div/form/div/div/div[1]/h1') \
                    .get_attribute('innerHTML')
                element = driver.find_element(By.XPATH, '//ul[@class="option-radio-group"]')

                prices = element.find_elements(By.XPATH, '//span[@class="option_price-num"]/span')
                prices = [price.get_attribute('innerHTML') for price in prices]
                
                colors = element.find_elements(By.XPATH, '//li/label')
                colors = [color.get_attribute('innerHTML') for color in colors]

                for i in range(len(prices)):
                    tmp = {}
                    tmp['color'] = colors[i+1]
                    tmp['price'] = prices[i]
                    tmp['url'] = url
                    tmp['name'] = name
                    tmp['rom'] = "unknown"
                    tmp['url_img'] = url_img
                    data.append(tmp)
                    #print(tmp)
            except Exception as e:
                continue
        driver.quit()
        return data


    def saveDataToLocalFile(self):
        path = os.path.join(os.getcwd(), 'data/', self.source, self.filename)
        with open(path, 'w') as f:
            f.write(json.dumps(self.data))
            f.close()
