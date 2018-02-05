# -- coding: utf-8 --
import scrapy

#Abrimos el  txt donde guardaremos los datos
f = open("output.txt","w")

class SpidetSpider(scrapy.Spider):
	name = 'spidet'
	allowed_domains = ['elpais.com']
	start_urls = ['https://elpais.com/']

#Coge la lista de diccionarios y saca la mayor longitud
	def maximo(self,list_content):
		l_len = []
		for d in list_content:
			l_len.append(d["len"])
		max_d = max(l_len)
		return max_d

#Esta funcion pasa los articulos admitidos y los pasa a una lista de diccionarios con el articulo y su longitud. 
#Maximo(). Saca el articulo acorde a la longitud maxima
	def get_art_mayor(self,list_content):
		list_len = []
		for art in list_content:
			d = {"len" :len(str(art)), "art":art}
			list_len.append(d)
		max_d = self.maximo(list_len)
		final_content = (item for item in list_len if item["len"] == max_d).next()
		return final_content

#Saca las urls de la web y las pone en formato valido ("https://elpais.com/" + url)
	def parse(self, response):
		urls = response.xpath('//section[starts-with(@class, "bloque_")]/div/div/div/article/div/h2[@class="articulo-titulo"]/a/@href').extract()
		global f
		for url in urls:
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_details)
		
#Con esta función sacamos los posibles titulos y articulos (ya que cada pagina tiene un formato diferente)
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

		list_titles = [t1,t2,t3,t4,t5,t6,t7,t8]
		
		c1 = response.xpath('//*[@class="articulo-cuerpo"]/p[not(@class="siguenos_opinion")]/text()').extract()
		c2 = response.xpath('//div[@class="row texto shareable"]/div/div/text()').extract()
		c3 = response.xpath('//*[@itemprop="articleBody"]/p[not(@class="siguenos_opinion")]/text()').extract()
		c4 = response.xpath('//*[starts-with(@class, "entry-content")]/p/text()').extract()
		c5 = response.xpath('//div[@class="post-contents"]/p/text()').extract()
		c6 = response.xpath('//*[@class="texto-galeria"]/p/text()').extract()
		c7 = response.xpath('//p[@dir="ltr"]/text()').extract()
		c8 = response.xpath('//*[@class="foto-texto"]/text()').extract()
		c9 = response.xpath('//div[@class="entradilla"]/p/text()').extract()

		list_content = [c1,c2,c3,c4,c5,c6,c7,c8,c9]

#Llamamos a una funcion seleccionamos el articulo correcto (algunas funciones devuelmen mas de un argumento)
		content = self.select_art(self,list_content)

#Seleccionamos el titulo correcto (algunas funciones devuelmen mas de un argumento)
		title = self.select_title(list_titles)
		
#Unimos las p seleccionadas 
		content = " ".join(content)
	
#Escribimos en nuestro fichero txt el titulo + el articulo, separados por "|"
		f.write(title+"|"+content+"\n")
		yield title

#Esta funcion comprueba que los titulos no esten vacios, o erroneos para sacar el valido
	def select_title(list_titles):
		final_title = "Título no identificado"
		for title in list_titles:
			if title != "" and title is not None and title != "\n":
				final_title = title

		return final_title.encode("utf-8")

#Esta funcion selecciona el o los articulos que no estan vacios, luego llama a otra funcion para seleccionar el valido y lo devuelve
	def select_art(self,list_content):
		final_content = "Título no identificado"
		accepted = []
		for content in list_content:
			if content != "" and content is not None and content!=t10:
				accepted.append(content)
		final_content = self.get_art_mayor(accepted)
		return final_content["art"].encode("utf-8")
	