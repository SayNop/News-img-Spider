import scrapy
import time
from News_img.items import NewsImgItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # 2.检测域名范围
    allowed_domains = ['hnr.cn']
    # 1.修改起始的url
    start_urls = ['http://news.hnr.cn/xwgqtj/201808/t20180817_3130286.html']

    def parse(self, response):
        # *************常规写法***************
        # 提取数据
        # 获取图片节点//*[@id="scroll"]/div[2]
        nodes = response.xpath('//div[@class="TRS_Editor"]//img')

        item = NewsImgItem()
        item['link'] = response.urljoin(nodes.xpath('./@src').extract_first())
        # 测试链接提取是否正常
        # print(item)
        yield item

        # 翻页id="nexttt"class="f12_fff"
        page_url = response.xpath('//a[@id="nexttt"]/@href').extract_first()
        print(page_url)
        # 中止条件
        if page_url != '#':
            next_url = response.urljoin(page_url)
            print(next_url)
            # 构建请求对象返回给引擎
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )

        # ***********使用移动端解析*************
        # 提取数据
        # 获取图片节点/html/body/div/div[11]/p[1]/mip-img/img
        # nodes = response.xpath('//mip-img/img')
        #
        # for node in nodes:
        #
        #     # 实例化节点
        #     item = NewsImgItem()
        #     item['link'] = nodes.xpath('.@src').extract_first()
        #     # 测试链接提取是否正常
        #     print(item)
        #     yield item
