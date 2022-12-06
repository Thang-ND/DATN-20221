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

def createDriver():
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    return driver
def crawl(destination):
    print("-------------------------")
    data = []
    driver = createDriver()
    # for category in apple_categories:
    urls = []
    driver.get(destination)
    # time.sleep(2)
    x_path = '//*[@id="__layout"]/div/div[3]/div[2]/div[1]/div[4]/div/div[1]/div[2]/a'
    for i in range(1):
        print("*")
        button = driver.find_element(By.XPATH, x_path)
        if button is None:
            break
        try:
            button.click()
        except:
            continue
        # time.sleep(5)


    items = driver.find_elements(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[2]/div[1]/div[3]/div[5]/div/div[1]/div/div/a')
    for i in items:
        urls.append(i.get_attribute('href'))
    # print(len(urls))
    # print(urls)
    driver.quit()
    for url in tqdm(urls):
        driver2 = createDriver()
        driver2.get(url)
        print('get url detail')
        # time.sleep(2)
   #     try:
        list_blocks = driver2.find_elements(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[2]/div/section/div/div[2]/div[2]/div[2]/div/a')
        list_link = [link.get_attribute('href') for link in list_blocks]
        driver2.quit()

        for link in list_link:
            flag = True
            while(flag):
                try:
                    driver3 = createDriver()
                    driver3.get(link)
                    # except Exception as e: 
                    #     print(e)
                    #     driver.get(link)
                    print('get url link 3')
                    # time.sleep(2)
                    name = driver3.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[2]/div/section/div/div[1]/div[1]/h1').get_attribute('innerHTML')
                    lists = driver3.find_elements(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[2]/div/section/div/div[2]/div[2]/div[3]/div[2]/ul/li/a/div')
                    colors = [l.find_element(By.TAG_NAME, 'strong').get_attribute('innerHTML') for l in lists]
                    prices = [l.find_element(By.TAG_NAME, 'span').get_attribute('innerHTML') for l in lists]
                    url_img = driver3.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[2]/div/section/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div/img').get_attribute('src')
                    for i in range(len(colors)):
                        tmp = {}
                        tmp['color'] = str(colors[i])
                        tmp['name'] = str(name)
                        tmp['rom'] = 'unknown'
                        tmp['ram'] = 'unknown'
                        if url_img is None:
                            url_img = 'unknown'
                        tmp['url_img'] = str(url_img)
                        tmp['price'] = str(re.sub(r'\D', '', prices[i]))
                        print(tmp)
                        data.append(tmp)
                    driver3.quit()
                    flag = False
                except Exception as e:
                    print("Retry")
                    pass


    return data
if __name__ == '__main__':
    print("start")
    flag = True
    data = []

    apple_categories = {
        'iphone': 'https://cellphones.com.vn/mobile/apple.html'
      
    }   
    for cat in apple_categories:
        tmp = None
        url = apple_categories[cat]
        print(url)
        # while(flag):
        #     try:
        #         tmp = crawl(url)
        #         flag = False
                
        #     except Exception as e: 
        #         print("Retry job crawler")
        #         pass
        tmp = crawl(apple_categories['iphone'])
        data.append(tmp)


    with open('./data.json', 'w') as f:
        f.write(json.dumps(data))
        f.close
