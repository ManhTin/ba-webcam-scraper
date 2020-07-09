# -*- coding: utf-8 -*-
import scrapy

class BergfexWebcamSpider(scrapy.Spider):
    # refreshes every 15min
    name = 'bergfex_webcam'
    allowed_domains = ['www.bergfex.ch/nendaz-4-vallees/webcams/c1310']
    start_urls = ['http://www.bergfex.ch/nendaz-4-vallees/webcams/c1310/']

    def parse(self, response):
        webcam = response.xpath("//img[@class='webcamimage-latest']")
        src = webcam.xpath(".//@src").get()
        yield {
            'src': src,
        }
