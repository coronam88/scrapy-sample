import scrapy
from scrapy_playwright.page import PageMethod

class StoresSpider(scrapy.Spider):
    name = 'stores'
    # allowed_domains = ['ubereats.com']
    # start_urls = ['https://ubereats.com/']


    def start_request(self):
        url = 'https://www.ubereats.com/store/subway-2473-hackworth-rd/fzEDE5hrV9uCv1fHwW17Fw'

        yield scrapy.Request(
            url = url,
            meta=dict(playwright=True, 
            playwright_include_page=True,
            # playwright_page_methods=[PageMethod('evaluate',"getByRole('button',{name:'Close'}).click()")]
        ))

    async def parse(self, response):
        # page = response.meta["playwright_page"]
        # print("PAGEEEEEEEEEEEEEEEE ",page)
        # await page.close()
        print("metaaaaaaaaaaaaaa", response.meta)


        
        print("#######################",response.css('button.ah.cd.ia.ib.i2.ic.bf.bg.bc.gi.b0.d7.id.ie').get())
        
        # for product in response.css('div.ah.am.ew').get():
        #     print("$$$$$$$$$$$$", product)
            
        #     # print('$$$$$$$$$$$$$$', product.css('div.ah.hk.bc.hl').get())
        #     """store_name
        #     store_address
        #     store_description
        #     store_price_range
        #     store_tags
        #     product_category
        #     product_name
        #     product_price
        #     """


    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
            

            