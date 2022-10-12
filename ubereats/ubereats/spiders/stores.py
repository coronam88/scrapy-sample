
import scrapy
from scrapy_playwright.page import PageMethod
import re
class StoresSpider(scrapy.Spider):
    name = 'stores'
    # allowed_domains = ['ubereats.com']
    # start_urls = ['https://ubereats.com/']


    def start_requests(self):
        url = 'https://www.ubereats.com/store/subway-2473-hackworth-rd/fzEDE5hrV9uCv1fHwW17Fw'
        # url = 'https://www.ubereats.com/store/dam-near-home/u8cEPsZ2XxiI5uxdDYIs1Q'

        yield scrapy.Request(
            url = url,
            meta=dict(playwright=True, 
            playwright_include_page=True,
            playwright_page_methods=[PageMethod('wait_for_selector','div.d9.da.d8.b0.db')]
        ))

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()
                
        # One li per product_category
        cat_list=[]
        # print(len(response.xpath(f'//*[@id="main-content"]/div[4]/div/div[4]/ul/li')))
        lis = None
        for cat in response.xpath(f'//*[@id="main-content"]/div[4]/div/div[4]/ul/li'):
            print("########### CATEGORY")
            category_name = cat.css('div::text').get()
            lis = cat.css('li ul li')
            for li in lis:
                prod = {}
                # print(li.css('span::text').getall())
                prod["product_name"] = " ".join(re.findall(r"[a-zA-Z]+", li.css('span::text').getall()[0]))
                prod["product_category"] = " ".join(re.findall(r"[a-zA-Z]+",category_name))
                prod["price"] = re.findall(r"[\.0-9]*$", li.css('span::text').getall()[1])[0]

                try:
                    prod["product_description"] = " ".join(re.findall(r"[a-zA-Z]+", li.css('span::text').getall()[2]))
                except:
                    prod["prod_description"] = ""
                try:
                    # print(li.css('picture img').attrib['src'])
                    prod["photo"] = li.css('picture source').attrib['srcset']
                except:
                    # print("no photo")
                    prod["photo"] = ""


                yield prod       
            
  
        """store_name
        store_address
        store_description
        store_price_range
        store_tags
        product_category
        product_name
        product_price
        """


    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
            

            