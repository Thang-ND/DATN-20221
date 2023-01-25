import scrapy 
import numpy as np
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

class IphoneSpider(scrapy.Spider):
    data = []
    name = 'thegioididong-iphone'
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    start_urls = ['https://www.thegioididong.com/dtdd-apple-iphone',
        'https://www.thegioididong.com/may-tinh-bang-apple-ipad',
        'https://www.thegioididong.com/laptop-apple-macbook',
        'https://www.thegioididong.com/dong-ho-thong-minh-apple'
    ]

    def parse(self, response):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        url = 'https://www.thegioididong.com'
        urls = response.xpath('//*[@class="main-contain"]/@href').getall()
        list_products = [url + e for e in urls]

        yield from response.follow_all(list_products, self.parse_info)

    def parse_info(self, response):
        colors = response.xpath('/html/body/section[1]/div[3]/div[2]/div[2]/div/a/text()').getall()
        for color in colors:
            item = {
                'name': response.xpath('/html/body/section[1]/h1/text()').get(),
                'price': response.xpath('//*[@class="box-price-present"]/text()').get(),
                'color': color,
                'url': response.request.url,
                'data': response.xpath('/html/body/section[1]/div[3]/div[2]/div[5]/ul').get()
            }
            self.data.append(item)
            #print(item)

    def crawl(self):
        settings = get_project_settings()
        settings.set('USER_AGENT','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')
        process = CrawlerProcess(settings)
        process.crawl(IphoneSpider)
        process.start()

    def getData(self):
        return self.data
    # def getMessageFromKafka(self):
    #     data = []
    #     for message in self.consumer:
    #         data.append(message.value)
    #     return data