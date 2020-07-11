# -*- coding: utf-8 -*-
import scrapy
from bachelor_thesis_scraper.items import WebcamImageItem

class GeierlayWebcamSpider(scrapy.Spider):
    # refreshes every 20s
    name = 'geierlay_webcam'
    allowed_domains = ['geierlay.de/besucherzentrum/webcam-parkplatz-besucherzentrum']
    start_urls = ['http://geierlay.de/besucherzentrum/webcam-parkplatz-besucherzentrum/']

    def parse(self, response):
        webcam = response.xpath("//img[@class='aligncenter']")
        src = webcam.xpath(".//@src").get()
        item_data = {
            'name': 'geierlay_webcam',
            'image_urls': [src],
        }
        yield WebcamImageItem(**item_data)
