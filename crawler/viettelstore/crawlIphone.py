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
import re


def crawl(destination):
    print("-------------------------")
    data = []
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)


    # for category in apple_categories:
    urls = []
    driver.get(destination)
    x_path = '//*[@id="div_Danh_Sach_San_Pham_loadMore_btn"]/a'
    for i in range(1):
        print("*")
        button = driver.find_element(By.XPATH, x_path)
        if button is None:
            break
        try:
            button.click()
        except:
            continue
        time.sleep(2)


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
            
            url_img = driver.find_element(By.XPATH, '//*[@id="sync-big"]/div[1]/div/div[1]/div/img').get_attribute('src')
        except Exception as e:
            url_img = 'unknown'
            print(e)
            continue

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
                #print(tmp)
                data.append(tmp)

    return data
if __name__ == '__main__':
    print("start")
    flag = True
    data = []

    apple_categories = {
        # 'iphone': 'https://viettelstore.vn/dtdd-apple-iphone?utm_source=website&utm_medium=sis',
        'ipad': 'https://viettelstore.vn/tablet-apple-ipad?utm_source=website&utm_medium=sis',
        'watch': 'https://viettelstore.vn/tbd-apple-watch?utm_source=website&utm_medium=sis',
        'airpods': 'https://viettelstore.vn/ket-qua-tim-kiem.html?keyword=airpods&utm_source=website&utm_medium=sis'
    }   
    for cat in apple_categories:
        tmp = None
        url = apple_categories[cat]
        print(url)
        while(flag):
            try:
                tmp = crawl(url)
                flag = False
                
            except Exception as e: 
                print("Retry job crawler")
                pass
        data.append(tmp)


    with open('./data.json', 'w') as f:
        f.write(json.dumps(data))
        f.close
