# -- coding: utf-8 --
import scrapy

f = open("output.txt","w")
class SpidetSpider(scrapy.Spider):
	name = 'spidet'
	allowed_domains = ['elpais.com']
	start_urls = ['https://elpais.com/']
	
	def maximo(self,l):
		l_len = []
		for d in l:
			l_len.append(d["len"])
		max_d = max(l_len)

		return max_d

	def get_art_mayor(self,lista):
		lista_len = []
		for art in lista:
			d = {"len" :len(str(art)), "art":art}
			lista_len.append(d)
		max_d = self.maximo(lista_len)
		art_final = (item for item in lista_len if item["len"] == max_d).next()
		return art_final

	def parse(self, response):
		urls = response.xpath('//section[starts-with(@class, "bloque_")]/div/div/div/article/div/h2[@class="articulo-titulo"]/a/@href').extract()
		global f
		for url in urls:
			url = response.urljoin(url)
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
		
		a1 = response.xpath('//*[@class="articulo-cuerpo"]/p[not(@class="siguenos_opinion")]/text()').extract()
		a2 = response.xpath('//div[@class="row texto shareable"]/div/div/text()').extract()
		a3 = response.xpath('//*[@itemprop="articleBody"]/p[not(@class="siguenos_opinion")]/text()').extract()
		a4 = response.xpath('//*[starts-with(@class, "entry-content")]/p/text()').extract()
		a5 = response.xpath('//div[@class="post-contents"]/p/text()').extract()
		a6 = response.xpath('//*[@class="texto-galeria"]/p/text()').extract()
		a7 = response.xpath('//p[@dir="ltr"]/text()').extract()
		a8 = response.xpath('//*[@class="foto-texto"]/text()').extract()
		a9 = response.xpath('//div[@class="entradilla"]/p/text()').extract()

		content = self.select_art(self,a1,a2,a3,a4,a5,a6,a7,a8,a9)

		content = " ".join(content)
		content = content.encode("utf-8")
		title = self.select_title(t1,t2,t3,t4,t5,t6,t7,t8)

		f.write(title+"|"+content+"\n")
		yield title

	def select_title(t1,t2,t3,t4,t5,t6,t7,t8,t9):
		final_title = "Título no identificado"
		list_titles = [t1,t2,t3,t4,t5,t6,t7,t8,t9]
		for title in list_titles:
			if title != "" and title is not None and title != "\n":
				final_title = title

		return final_title.encode("utf-8")

	def select_art(self,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10):
		final_title = "Título no identificado"
		list_titles = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
		admitidos = []
		for title in list_titles:
			if title != "" and title is not None and title!=t10:
				admitidos.append(title)
		final_title = self.get_art_mayor(admitidos)
		return final_title["art"]	