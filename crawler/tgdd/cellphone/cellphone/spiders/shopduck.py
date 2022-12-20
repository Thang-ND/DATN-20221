import scrapy 
import numpy as np

class IphoneSpider(scrapy.Spider):
    name = 'shopduck'
    start_urls = ['https://shopdunk.com/iphone']

    def parse(self, response):
        phone_links = response.xpath('//div[@class="elementor-widget-container"]/h3/a/@href').getall()
        phone_links = np.array(phone_links)
        phone_links = np.unique(phone_links)
        phone_links = list(phone_links)

        yield from response.follow_all(phone_links, self.parse_phone)

    def parse_phone(self, response): 
        yield {
            "name": response.xpath('//*[@id="content"]/div/div[2]/div/section[2]/div/div/div[2]/div/div/section[1]/div/div/div[1]/div/div/div/div/h1/text()').get(),
            "price": response.xpath('//*[@id="content"]/div/div[2]/div/section[2]/div/div/div[2]/div/div/section[2]/div/div/div/div/div/div[1]/div/p/span/ins/span/bdi/text()').get(),
            "url_img": response.xpath('//*[@id="content"]/div/div[2]/div/section[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div/div/div[1]/img/@src').extract(),
            "link": response.request.url,
            #"data": response.xpath('//*[@id="myTabContent"]').getall(),
        }