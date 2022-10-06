import scrapy


class PlacesSpider(scrapy.Spider):
    name = 'places'
    allowed_domains = ['ubereats.com']
    start_urls = ['http://ubereats.com/']

    def parse(self, response):
        pass
