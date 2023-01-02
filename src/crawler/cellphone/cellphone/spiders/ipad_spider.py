import scrapy 
import numpy as np

class IphoneSpider(scrapy.Spider):
    name = 'tragopdidong-ipad'
    start_urls = ['http://tragopdidong.vn/ipad-2-3-4', 'http://tragopdidong.vn/san-pham/ipad-mini', 'http://tragopdidong.vn/san-pham/ipad-air']

    def parse(self, response):
        phone_links = response.xpath('//a[contains(@href, ".html")]/@href').getall()
        phone_links = np.array(phone_links)
        phone_links = np.unique(phone_links)
        phone_links = list(phone_links)

        yield from response.follow_all(phone_links, self.parse_phone)

    def parse_phone(self, response): 
        yield {
            "name": response.xpath('/html/body/div[3]/div/div[2]/div[1]/div[2]/div[2]/div/h1/text()').get(),
            "price": response.xpath('//*[@class="giagia"]/text()').get(),
            "url_img": response.xpath('//*[@id="img_01"]/@src').extract(),
            "link": response.request.url,
            "data": response.xpath('//*[@id="myTabContent"]').getall(),
        }