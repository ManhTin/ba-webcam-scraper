# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
from urllib.parse import urlparse

from scrapy.pipelines.images import ImagesPipeline

class BachelorThesisScraperPipeline:
    def process_item(self, item, spider):
        return item


class WebcamImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return urlparse(request.url).hostname + "/" + current_date_time + '.jpg'
