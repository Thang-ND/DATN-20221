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
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    urls = []
    products = []
    apple_categories = {
        'iphone': 'https://shopdunk.com/iphone'
    }
    # for category in apple_categories:
    driver.get('https://shopdunk.com/iphone')
    print("Waiting...")
    time.sleep(3)

    items = driver.find_elements(By.XPATH,'//div[@class="elementor-widget-container"]/h3/a')
    urls = [item.get_attribute("href") for item in items]
    
    for url in urls:
        try:
            driver.get(url)
            product = {}
            product['name'] = driver.find_element(By.XPATH, '//h1[contains(@class, "product_title")]').get_attribute("innerHTML")
            product['price'] = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/section[2]/div/div/div[2]/div/div/section[2]/div/div/div/div/div/div[1]/div/p/span/ins/span/bdi').get_attribute("innerHTML").split("<span")[0]
            product['url'] = url
            product['url_img'] = 'unknown'
            product['color'] = 'unknown'
            print(product)
            products.append(product)
        except Exception as e:
            continue
    driver.quit()
    return products
if __name__ == '__main__':
    print("start")
    data = crawl()
    with open('./data.json', 'w') as f:
        f.write(json.dumps(data))
        f.close
    # print("end")
    # print(len(data))
    # # print(urls)
