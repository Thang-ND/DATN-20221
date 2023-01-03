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
    products = []
    options = FirefoxOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    urls = []
    apple_categories = {
        'iphone': 'https://shopdunk.com/iphone'
    }
    # for category in apple_categories:
    driver.get('https://shopdunk.com/iphone')
    time.sleep(3)

    items = driver.find_elements(By.XPATH,'//div[@class="product-title"]/a')
    urls = [item.get_attribute("href") for item in items]


    for url in urls:
        #try:
            driver.get(url)
            sub_urls = driver.find_elements(By.CLASS_NAME,\
                 'option-list.darkcontrols')
            
            # sub_urls = driver.find_elements(By.XPATH, '//div[@class="attributes"]/dl/dd[1]/ul/li/a')
            # sub_urls = driver.find_elements(By.XPATH, '//dd[contains(@id, "product_attribute_input_")]/li/a')
            # sub_urls = [sub.get_attribute('@href') for sub in sub_urls]
            print(len(sub_urls))
            break
            # for sub in sub_urls:
            #     print("=============")
            #     print(sub)
            #     driver.get(sub)
            #     time.sleep(1)

            #     colorClick = driver.find_elements(By.XPATH, '//ul[contains(@id,"color-squares-")]/li/label/input')

            #     for ratio in colorClick:
            #         ratio.click()
            #         time.sleep(1)
            #         print("A")
            #         product = {}
            #         product['name'] = driver.find_element(By.XPATH, '//span[contains(@class, "main-name")]') \
            #             .get_attribute("innerHTML")
            #         product['price'] = driver.find_element(By.XPATH, '//div[contains(@class,"product-price")]/span') \
            #             .get_attribute("innerHTML")
            #         product['url'] = driver.current_url
            #         product['url_img'] = 'unknown'
            #         product['color'] = 'unknown'
            #         print(product)
            #         products.append(product)
        # except Exception as e:
        #     continue
    driver.quit()
    return products
if __name__ == '__main__':
    print("start")
    data = crawl()
    with open('./data.json', 'w') as f:
        f.write(json.dumps(data))
        f.close

