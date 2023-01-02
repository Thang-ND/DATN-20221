import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from tqdm import tqdm
from selenium.webdriver.firefox.options import Options as FirefoxOptions


if __name__ == '__main__':

    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    urls = []
    products = []
    apple_categories = {
        'iphone': 'https://dienmaycholon.vn/dien-thoai-di-dong-apple'
    }


    for category in apple_categories:    
        driver.get(apple_categories[category])
        try:
            for i in range(2):
                bt = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[4]/div/div[2]/div[4]/div/div[2]/button')
                bt.click()
                time.sleep(1)
        except Exception as e:
            print(e)
            pass
        items = driver.find_elements(By.XPATH, '//div[@class="product"]/div[2]/a[1]')
        for item in items:
            urls.append(item.get_attribute('href'))

    for url in tqdm(urls):
        driver.get(url)

        sub_urls = driver.find_elements(By.XPATH, '//div[@class="many_size_pro"]/a')
        sub_urls = [sub.get_attribute('href') for sub in sub_urls]

        for sub in sub_urls:
            driver.get(sub)
            color = []
            price = []

            eles = driver.find_elements(By.XPATH, '//div[@class="many_size_pro"][2]/a')
            list_sub_urls = [e.get_attribute('href') for e in eles]
            for i in eles:
                color.append(i.find_element(By.CLASS_NAME, 'size-pro').get_attribute('innerHTML'))
            for i in eles:
                price.append(i.find_element(By.CLASS_NAME, 'price-pro').get_attribute('innerHTML'))

            product = {}
            name = driver.find_element(By.XPATH, '//div[@class="name_pro_detail"]/h1').get_attribute('innerHTML')
            product['name'] = name
            product['url'] = url

            for i in range(len(color)):
                product = {}
                product['name'] = name
                product['url'] = list_sub_urls[i]
                product['color'] = color[i]
                product['price'] = price[i]
                print(product)
                products.append(product)
    # with open('./Data.json', 'w') as f:
    #     f.write(json.dumps(products))
    #     f.close()
    driver.quit()