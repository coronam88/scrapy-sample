import scrapy


class UberstoreSpider(scrapy.Spider):
    name='uberstore'

    def start_request(self):
        url = 'https://www.ubereats.com/store/subway-2473-hackworth-rd/fzEDE5hrV9uCv1fHwW17Fw'

        yield scrapy.Request(
            url = url,
            meta=dict(playwright=True, 
            playwright_include_page=True
        ))


        
    async def parse(self, response):
        print("metaaaaaaaaaaaaaaa", response.meta)
        return 