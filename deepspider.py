# -*- coding: utf-8 -*-
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "deepspider"

    def start_requests(self):
     
        f = open('elpais.txt', 'r')
        urls = f.readlines()
       
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'articulo.txt'
        with open(filename, 'wb') as f:
            lista1 = response.xpath('//h1').extract()
            lista2 = response.xpath('//div[@class="articulo-cuerpo"]').extract()
            lista3 = []
            size = len(lista3)
            for i in xrange(size):                    
                lista3 = var = lista1[i] + "\t" + lista2[i] + "\n"
                lista3.append(var)
                f.write(lista3+'\n')
