from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from tqdm import tqdm

def crawl():
    options = FirefoxOptions()
    #options.add_argument('--headless')
    driver = webdriver.Firefox()
    pages = ['https://www.gsmarena.com/apple-phones-48.php',
        'https://www.gsmarena.com/apple-phones-f-48-0-p2.php',
        'https://www.gsmarena.com/apple-phones-f-48-0-p3.php'
    ]
    data = []

    for page in pages:
        driver.get(page)
        links = driver.find_elements(By.XPATH, '//a[contains(@href, ".php")]')
        links = [link.get_attribute('href') for link in links]
        urls = []
        for i in range(len(links)):
            if 'php3' in links[i]:
                continue
            urls.append(links[i])
        print(len(urls))
        for link in tqdm(urls):
            try:
                print("get link "+ link)
                driver.get(link)
                table = driver.find_element(By.XPATH, '//div[@id="specs-list"]').get_attribute('innerHTML')
                name = driver.find_element(By.XPATH, '//h1[@class="specs-phone-name-title"]').get_attribute('innerHTML')
                item = {}
                item['name'] = name
                item['data'] = table
                print(item)
                data.append(item)
            except Exception as e:
                print(e)
                pass 

    driver.quit()
    return data

if __name__ == '__main__':
    data = crawl()
    with open('./info.json', 'w') as f:
        f.write(json.dumps(data))
        f.close