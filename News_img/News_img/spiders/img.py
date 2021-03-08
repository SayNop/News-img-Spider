import scrapy


class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['hnr.cn']
    start_urls = ['http://hnr.cn/']

    def parse(self, response):
        pass
