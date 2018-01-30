import scrapy
from scrapy.selector import HtmlXPathSelector

class QuotesSpider(scrapy.Spider):
    name = "crawler"

    def start_requests(self):
        urls = [
            'http://elpais.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
	hxs = HtmlXPathSelector(response)
        filename = 'elpais.txt'
        with open(filename, 'wb') as f:
		lista_urls = hxs.select('//h2/a/@href').extract()
		for url in lista_urls:
			f.write(url+"\n")
