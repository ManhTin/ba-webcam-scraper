# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BachelorThesisScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WebcamImageItem(scrapy.Item):
    name = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
