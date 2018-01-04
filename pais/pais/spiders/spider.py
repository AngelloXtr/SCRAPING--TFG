import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pais.items import PaisItem
from scrapy.exceptions import CloseSpider

class paisSpider(CrawlSpider):
    name = 'pais'
    item_count = 0
    allowed_domain = ['https://elpais.com/']
    start_urls = ['www.elpais.com']
    
    rules = {
        
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@class="articulo-titulo"]')) callback = 'parse_item', follow = False)
    }
    
    def parse_item(self, response):
        ml_item = paisItem()
        ml_item['titulo'] = response.xpath('normalize-space(//*[@class="articulo-titulo"])/text()').extract()
        ml_item['url'] = response.xpath('//*[@class="articulo-titulo"]/a/@href').extract()
        
        self.item_count += 1
        if self.item_count > 200:
            raise CloseSpider('item_exeeded')
        
        yield ml_item
        
        
        
        