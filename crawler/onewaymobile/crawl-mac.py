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
        'mac': 'https://onewaymacbook.vn/macbook-moi'
    }

    # try:
    for category in apple_categories:    
        driver.get(apple_categories[category])
        button = driver.find_element(By.XPATH, '//a[@id="load_more_button"]')
        try:
            button.click()
        except Exception as e:
            print(e)
        items = driver.find_elements(By.CLASS_NAME, 'image-product')
        for item in items:
            urls.append(item.get_attribute('href'))
        print(len(urls))
        for url in tqdm(urls):
            driver.get(url)
            sub_items = driver.find_elements(By.XPATH,'//li[@class="col-md-4"]/a')
            sub_items = [item.get_attribute('href') for item in sub_items]
            print(sub_items)
            print("+========================================================+")

            for sub in sub_items:
                print("get detailed item")
                driver.get(sub)
                name = driver.find_element(By.XPATH, '//div[@class="title-product"]/h1').get_attribute('innerHTML')
                print(name)
                data = driver.find_element(By.XPATH, '//table[@class="charactestic_table"]').text
                pairs = driver.find_elements(By.XPATH, '//div[contains(@class, "color-product")]/div[1]/div[2]')
                p_colors = driver.find_elements(By.XPATH, '//span[@class="text-center"]')
                colors = []
                prices = []
                for pair in range(len(pairs)):
                    try: 
                        #tmp = pair.find_elements(By.TAG_NAME, 'span')
                        colors.append(pairs[pair].get_attribute('innerHTML'))
                        prices.append(p_colors[pair].get_attribute('innerHTML'))
                    except Exception as e:
                        continue
                
                for i in range(len(colors)):
                    product = {}    
                    product['name'] = name 
                    product['url'] = sub
                    product['url_img'] = 'unknown'
                    product['rom'] = 'unknown'
                    product['ram'] = 'unknown'
                    product['color'] = colors[i]
                    product['price'] = prices[i]
                    product['info'] = data
                    # print(product)
                    products.append(product)
    # except Exception as e:
    #     print(e)
    #     pass
    

    json_products = json.dumps(products)
    with open("./Data-mac.json",'w') as f:
        f.write(json_products)
        f.close()
    driver.quit()