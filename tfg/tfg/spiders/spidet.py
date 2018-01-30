# -*- coding: utf-8 -*-
import scrapy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#from tfg.items import TfgItem
f = open("output.txt","w")
class SpidetSpider(scrapy.Spider):
	name = 'spidet'
	allowed_domains = ['elpais.com']
	start_urls = ['https://elpais.com/']
	

	def parse(self, response):
		urls = response.xpath('//section[starts-with(@class, "bloque_")]/div/div/div/article/div/h2[@class="articulo-titulo"]/a/@href').extract()
		global f
		for url in urls:
			url = response.urljoin(url)
			self.log('En: ' + url)
			yield scrapy.Request(url=url, callback=self.parse_details)
		

	def parse_details(self, response):
		global f
		t1 = response.xpath('//*[@id="articulo-titulo"]/text()').extract_first()
		t2 = response.xpath('//*[@id="titulo_noticia"]/text()').extract_first()
		t3 = response.xpath('//*[@id="entry-title"]/text()').extract_first()
		t4 = response.xpath('//*[@class="titulo_noticia"]/text()').extract_first()
		t5 = response.xpath('//*[@class="entry-title"]/text()').extract_first()
		t6 = response.xpath('//div[@class="titular cf"]/h1/text()').extract_first()
		t7 = response.xpath('//*[@class="articulo-titulo"]/text()').extract_first()
		t8 = response.xpath('//div[@class="single-title"]/div/h1/text()').extract_first()
		d = {
			'title': self.select_title(t1,t2,t3,t4,t5,t6,t7,t8)
			#'content': response.xpath('//p/text()').extract()
		}
		f.write(str(d)+"\n")
		yield d

	def select_title(t1,t2,t3,t4,t5,t6,t7,t8,t9):
		final = "Título no identificado"
		list_titles = [t1,t2,t3,t4,t5,t6,t7,t8,t9]
		for title in list_titles:
			if title != "" and title is not None and title != "\n":
				final_title = title
		return final_title