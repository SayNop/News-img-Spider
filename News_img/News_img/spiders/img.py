import scrapy


class ImgSpider(scrapy.Spider):
    name = 'img'
    # 2.检测域名范围
    allowed_domains = ['hnr.cn']
    # 1.修改起始的url
    start_urls = ['http://hnr.cn/']

    def parse(self, response):
        # 提取数据
        # 获取图片节点
        nodes = response.xpath('//div[@class="TRS_Editor"]/p[1]/font/img')
        # 翻页
