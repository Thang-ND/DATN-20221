import scrapy 
import numpy as np

class IphoneSpider(scrapy.Spider):
    name = 'info-spider'
    start_urls = ['https://www.gsmarena.com/apple-phones-48.php']

    def parse(self, response):
        phone_links = response.xpath('//a[contains(@href, ".php")]/@href').getall()
        phone_links = np.array(phone_links)
        phone_links = np.unique(phone_links)
        phone_links = list(phone_links)
        url = 'https://www.gsmarena.com/'
        urls = [url + link for link in phone_links]

        yield from response.follow_all(urls, self.parse_phone)

    def parse_phone(self, response): 
        tables = response.xpath('//*[@id="specs-list"]/table').getall()
        yield {
            "name": response.xpath('//h1[@class="specs-phone-name-title"]/text()').get(),
            "network": tables[1],
            "launch": tables[2],
            "body": tables[3],
            "display": tables[4],
            "platform": tables[5],
            "memory": tables[6],
            "main-camera": tables[7],
            "selfie-camera": tables[8],
            "sound": tables[9],
            "comms": tables[10],
            "features": tables[11],
            "battery": tables[12],
            "misc": tables[13]
        }