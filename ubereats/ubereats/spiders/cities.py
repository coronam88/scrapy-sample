import scrapy
from scrapy_playwright.page import PageMethod


class CitiesSpider(scrapy.Spider):
    name = 'cities'
    allowed_domains = ['ubereats.com']
    start_urls = ['https://ubereats.com/']
    BASE_URL='https://ubereats.com'

    def start_requests(self):
        url = 'https://www.ubereats.com/city/albany-wi'

        yield scrapy.Request(
            url = url,
            meta=dict(playwright=True, 
            playwright_include_page=True,
            playwright_page_methods=[PageMethod('wait_for_selector', 'div.hj.ic.id')])
        )
    
    async def parse(self, response):    
        for city in response.css('div.hj.ic.id'):
            print("################",city.css('div').get())
            store_name = city.css('h3.ie.dc.ae.cd::text').get()
            store_address = city.css('span.ba.bx.dj.c5.in.eb.ci.cg::text').get()
            store_description = city.css('div.ba.bx.dj.c5.in.eb.cg.ea::text').get()
            store_url = city.css('a').attrib['href']

            yield{
                "store_name":store_name,
                "store_address":store_address,
                "store_description":store_description,
                "store_url":self.BASE_URL + store_url
            }
            
        