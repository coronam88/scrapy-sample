
import scrapy
from scrapy_playwright.page import PageMethod
import re
class StoresSpider(scrapy.Spider):
    name = 'stores'
    # allowed_domains = ['ubereats.com']
    # start_urls = ['https://ubereats.com/']


    def start_requests(self):
        # url = 'https://www.ubereats.com/store/subway-2473-hackworth-rd/fzEDE5hrV9uCv1fHwW17Fw'
        url = 'https://www.ubereats.com/store/dam-near-home/u8cEPsZ2XxiI5uxdDYIs1Q'

        yield scrapy.Request(
            url = url,
            meta=dict(playwright=True, 
            playwright_include_page=True,
            playwright_page_methods=[PageMethod('wait_for_selector','div.d9.da.d8.b0.db')]
        ))

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        # main_div = response.css('div.d6')
        # main_div = response.xpath('//*[@id="main-content"]/div[4]/div/div[4]')
        # print("MAIN_DIV",len(main_div))
        # main_ul = main_div.css('ul')
        # main_ul = response.xpath('//*[@id="main-content"]/div[4]/div/div[4]/ul')
        # print("MAIN_UL",len(main_ul))

                
        # One li per product_category
        cat_list=[]
        print(len(response.xpath(f'//*[@id="main-content"]/div[4]/div/div[4]/ul/li')))
        lis = None
        for cat in response.xpath(f'//*[@id="main-content"]/div[4]/div/div[4]/ul/li'):
            print("########### CATEGORY")
            lis = cat.css('li').getall()
            print(lis[0].css('ul'))

       

















            # category_name = cat.css('div::text').get()
            # prods = cat.css('span::text').getall()            
            # for i, prod in enumerate(prods):
            #     prod_dict = {}
            #     try:
            #         if i % 2 == 0:
            #             # TODO: url de la imagen y url del producto en si
            #             prod_dict["product_name"] = " ".join(re.findall(r"[a-zA-Z]+",prods[i]))
            #             prod_dict["price"] = re.findall(r"[\.0-9]*$", prods[i+1])[0]
            #             prod_dict["product_category"] = " ".join(re.findall(r"[a-zA-Z]+",category_name))
                        
            #             yield prod_dict
            #     except:
            #         print("#################### ERROR")

        
       
            
  
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
            

            