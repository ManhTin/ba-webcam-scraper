# -*- coding: utf-8 -*-
import scrapy


class OlympicNpWebcamSpider(scrapy.Spider):
    # refreshes every 1min
    name = 'olympic_np_webcam'
    allowed_domains = ['www.nps.gov/media/webcam']
    start_urls = ['http://www.nps.gov/media/webcam/view.htm?id=81B46260-1DD8-B71B-0B7A7B41BF33172A']

    def parse(self, response):
        webcam = response.xpath("//img[@class='Webcam__Image']")
        src = webcam.xpath(".//@src").get()
        yield {
            'src': src,
        }
