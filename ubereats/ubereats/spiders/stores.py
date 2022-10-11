import scrapy
from scrapy_playwright.page import PageMethod

class StoresSpider(scrapy.Spider):
    name = 'stores'
    allowed_domains = ['ubereats.com']
    start_urls = ['http://ubereats.com/']


    def start_request(self):
        url = 'https://www.ubereats.com/store/dam-near-home/u8cEPsZ2XxiI5uxdDYIs1Q'

        yield scrapy.Request(url=url, meta=dict(playwright=True, playwright_include_page=True, playwright_page_methods=[PageMethod('wait_for_selector','div.d6')]))

    async def parse(self, response):
        print("################", response.css('div.d6'))
        for product in response.css('div.d6'):
            print('$$$$$$$$$$$$$$', product.css('div.ah.dj.g1.hm.ai').get())
            """store_name
            store_address
            store_description
            store_price_range
            store_tags
            product_category
            product_name
            product_price
            """
            return