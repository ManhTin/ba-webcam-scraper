# -*- coding: utf-8 -*-
import scrapy


class GeierlayWebcamSpider(scrapy.Spider):
    # refreshes every 20s
    name = 'geierlay_webcam'
    allowed_domains = ['geierlay.de/besucherzentrum/webcam-parkplatz-besucherzentrum']
    start_urls = ['http://geierlay.de/besucherzentrum/webcam-parkplatz-besucherzentrum/']

    def parse(self, response):
        webcam = response.xpath("//img[@class='aligncenter']")
        src = webcam.xpath(".//@src").get()
        yield {
            'src': src,
        }
