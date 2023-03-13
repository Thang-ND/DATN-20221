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
from kafka import KafkaConsumer
from kafka import KafkaProducer


class Store24h(Crawler):
    def __init__(self, source):
        super().__init__(source)
        #print(self.source)
        self.data = []
        self.filename = date.today().strftime(self.source+"%Y%m%d.json")
        self.producer =  KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], \
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        self.consumer = KafkaConsumer(self.source,bootstrap_servers=['127.0.0.1:9092'], \
            auto_offset_reset='earliest', \
            enable_auto_commit=True,\
            group_id='hust-0',consumer_timeout_ms=10000,\
            value_deserializer=lambda x: json.loads(x.decode('utf-8')))

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
                    # name = driver.find_element(By.XPATH, '//h1[@class="pull-left"]').get_attribute('innerHTML')
                    name = driver.find_element(By.XPATH, '//*[@id="main_container"]/div/div[1]/div[1]/div[1]/h1').get_attribute('innerHTML')
                    for i in range(len(colors)):
                        for j in range(len(roms)):
                            product = {}
                            product['name'] = name
                            product['rom'] = roms[j]
                            product['ram'] = 'unknown'
                            product['link'] = url
                            product['price'] = prices[j]
                            product['color'] = colors[i]
                            #print(product)
                            self.producer.send(self.source, value=product)
                            #self.data.append(product)
                except Exception as e:
                    print(e)
                    continue
        driver.quit()
        #return self.data


    def saveDataToLocalFile(self):
        path = os.path.join(os.getcwd(), 'data/raw_data/', self.source, self.filename)
        with open(path, 'w') as f:
            f.write(json.dumps(self.data))
            f.close()
    def saveDataToLocalFile2(self, df):
        path = os.path.join(os.getcwd(), 'data/raw_data/', self.source, self.filename)
        with open(path, 'w') as f:
            f.write(json.dumps(df))
            f.close()
        return path 
    def getMessageFromKafka(self):
        data = []
        for message in self.consumer:
            data.append(message.value)
        return data
