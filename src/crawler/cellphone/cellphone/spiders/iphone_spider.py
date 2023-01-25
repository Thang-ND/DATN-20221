import scrapy 
import numpy as np
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json

class IphoneSpider(scrapy.Spider):
    name = 'tragopdidong-iphone'
    start_urls = ['http://tragopdidong.vn/iphone']
    producer =  KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], \
                            value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    consumer = KafkaConsumer(name,bootstrap_servers=['127.0.0.1:9092'], \
        auto_offset_reset='earliest', \
        enable_auto_commit=True,\
        group_id='hust-0',consumer_timeout_ms=10000,\
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))    

    def parse(self, response):
        phone_links = response.xpath('//a[contains(@href, ".html")]/@href').getall()
        phone_links = np.array(phone_links)
        phone_links = np.unique(phone_links)
        phone_links = list(phone_links)

        yield from response.follow_all(phone_links, self.parse_phone)

    def parse_phone(self, response): 
        item =  {
            'name': response.xpath('/html/body/div[3]/div/div[2]/div[1]/div[2]/div[2]/div/h1/text()').get(),
            'price': response.xpath('//*[@class="giagia"]/text()').get(),
            'url_img': response.xpath('//*[@id="img_01327"]/@src').extract(),
            'link': response.request.url,
            'data': response.xpath('//*[@id="myTabContent"]').getall(),
        }
        self.producer.send(self.name, item)

    def crawl(self):
        settings = get_project_settings()
        settings.set('USER_AGENT','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')
        process = CrawlerProcess(settings)
        process.crawl(IphoneSpider)
        process.start()

    def getMessageFromKafka(self):
        data = []
        for message in self.consumer:
            data.append(message.value)
        return data