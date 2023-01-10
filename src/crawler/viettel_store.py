from .crawler import Crawler 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json 
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from tqdm import tqdm
import datetime
from datetime import date
import os
import re
from kafka import KafkaConsumer
from kafka import KafkaProducer


class ViettelStore(Crawler):
    def __init__(self, source):
        super().__init__(source)
        #print(self.source)
        self.data = []
        self.filename = date.today().strftime(self.source+"%Y%m%d.json")
        self.url = 'https://viettelstore.vn/dtdd-apple-iphone?utm_source=website&utm_medium=sis'

        self.producer =  KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], \
                        value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        self.consumer = KafkaConsumer(self.source,bootstrap_servers=['127.0.0.1:9092'], \
            auto_offset_reset='earliest', \
            enable_auto_commit=True,\
            group_id='hust-0',consumer_timeout_ms=10000,\
            value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    def crawl(self):
        destination = self.url
        data = []
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)


        # for category in apple_categories:
        urls = []
        driver.get(destination)
        x_path = '//*[@id="div_Danh_Sach_San_Pham_loadMore_btn"]/a'
        try:
            for i in range(1):
                button = driver.find_element(By.XPATH, x_path)
                if button is None:
                    break
                button.click()
                time.sleep(2)
        except Exception as e:
            print(e)
            pass


        items = driver.find_elements(By.CLASS_NAME, 'ProductList3Col_item')
        for i in items:
            urls.append(i.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        print(len(urls))
        for url in tqdm(urls):
            driver.get(url)
            try:
                bars = driver.find_element(By.XPATH, '//*[@id="owl-list-version"]/div[1]/div')
                list_blocks = bars.find_elements(By.CLASS_NAME, 'owl-item')
                list_blocks2 = bars.find_elements(By.XPATH, '//*[@id="owl-list-version"]/div[1]/div/div/a/strong')
                names = [c.find_element(By.TAG_NAME, 'div').get_attribute('innerHTML') for c in list_blocks]
                # print(names)
                prices = [p.get_attribute('innerHTML') for p in list_blocks2]
                # print(prices)

                color_elements = driver.find_element(By.CLASS_NAME, 'child_box')
                list_colors = color_elements.find_elements(By.CLASS_NAME, 'title-color')
                colors = [c.get_attribute('innerHTML') for c in list_colors]
                # print(colors)
                
                url_img = 'unknown'


                for i in range(len(names)):
                    for j in range(len(colors)):
                        tmp = {}
                        tmp['color'] = colors[j]

                        tmp['url'] = url
                        tmp['name'] = names[i]
                        tmp['rom'] = "unknown"
                        tmp['url_img'] = url_img
                        pre_price = prices[i].split('<')[0]
                        tmp['price'] = re.sub(r'\D', '', pre_price)
                        self.producer.send(self.source, tmp)
                        #print(tmp)
                        data.append(tmp)
            except Exception as e:
                print(e)
                continue
        driver.quit()
        #return data

    def saveDataToLocalFile(self):
        path = os.path.join(os.getcwd(), 'data/', self.source, self.filename)
        with open(path, 'w') as f:
            f.write(json.dumps(self.data))
            f.close()

    def getMessageFromKafka(self):
        data = []
        for message in self.consumer:
            data.append(message.value)
        return data           
