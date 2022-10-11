import scrapy
from scrapy_playwright.page import PageMethod


class PlacesSpider(scrapy.Spider):
    name = 'places'
    allowed_domains = ['ubereats.com']
    start_urls = ['https://ubereats.com/']
    BASE_URL='https://ubereats.com'
    

    def start_requests(self):
        url = 'https://www.ubereats.com/location'

        yield scrapy.Request(
            url = url,
            meta=dict(playwright=True,
            playwright_include_page=True,
            # playwright_page_coroutines=[PageCoroutine('wait_for_selector', 'div.ah.bf.b6')]
            # playwright_page_methods=[PageMethod('wait_for_selector','div.ah.bf.b6')]
            playwright_page_methods=[PageMethod('wait_for_selector','div.fo.fp')]
        ))

        
    async def parse(self, response):
        for place in response.css('div.fo.fp'):
            city_base_url = place.css('a').attrib['href']
            city_name = place.css('span::text').get()

            if 'city' in city_base_url:
                yield {
                    'city_name': city_name,
                    'city_url': self.BASE_URL + city_base_url,
                }

            #TODO:
            """if location in city_base_url we get the urls for the locations of other countries
            For example
            /mx/location is for Mexico
            """
        