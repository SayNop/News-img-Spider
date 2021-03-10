# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request

from News_img.settings import IMAGES_STORE
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NewsImgPipeline(object):
    def process_item(self, item, spider):
        return item


class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        url = item['link']

        return [Request(url)]

    def file_path(self, request, response=None, info=None):
        # 创建保存图片的文件夹
        if not os.path.exists(IMAGES_STORE):
            os.mkdir(IMAGES_STORE)

        # 截取url中的图片名
        name = request.url.split('/')[-1]

        # 拼接路径
        img_path = os.path.join(IMAGES_STORE,name)
        print(img_path)
        return img_path
