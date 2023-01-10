from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from tqdm import tqdm
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from json import dumps
import time
import re


def crawl():
    destination = 'https://cellphones.com.vn/mobile/apple.html'
    data = []
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    # for category in apple_categories:
    urls = []
    driver.get(destination)
    x_path = '/html/body/div[1]/div/div/div[3]/div[2]/div/div[4]/div[5]/div/div[2]/a'
    try:
        for i in range(2):
            print("*")
            button = driver.find_element(By.XPATH, x_path)
            button.click()
            time.sleep(2)
    except Exception as e: 
        pass



    items = driver.find_elements(By.XPATH, '//div[@class="product-info"]/a')
    for i in items:
        urls.append(i.get_attribute('href'))


    for url in tqdm(urls):
        try:
            sub_urls = []
            while(len(sub_urls)==0):
                driver.get(url)
                time.sleep(2)
                sub_urls = driver.find_elements(By.XPATH, '//div[@class="list-linked"]/a')
                sub_urls = [sub.get_attribute('href') for sub in sub_urls]
                #print(sub_urls)

            for sub in sub_urls:
                driver.get(sub)
                name = driver.find_element(By.XPATH, '//div[@class="box-product-name"]/h1').get_attribute('innerHTML')
                listObject = driver.find_elements(By.XPATH, '//ul[@class="list-variants"]/li')
                colors = [e.find_element(By.TAG_NAME, 'strong').get_attribute('innerHTML') for e in listObject]
                prices = [e.find_element(By.TAG_NAME, 'span').get_attribute('innerHTML') for e in listObject]


                for i in range(len(colors)):
                    product = {}
                    product['name'] = name
                    product['color'] = colors[i]
                    product['price'] = prices[i]
                    product['url'] = sub
                    #print(product)
                    data.append(product)
        except Exception as e:
            continue


    driver.quit()
    return data
if __name__ == '__main__':
    data = crawl()

    with open('./data.json', 'w') as f:
        f.write(json.dumps(data))
        f.close
