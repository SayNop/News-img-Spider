import scrapy
from News_img.items import NewsImgItem


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

        item = NewsImgItem()
        item['link'] = response.urljoin(nodes.xpath('./@src').extract_first())
        # 测试链接提取是否正常
        # print(item)
        # 翻页
