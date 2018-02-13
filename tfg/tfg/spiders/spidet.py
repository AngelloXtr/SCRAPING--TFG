# -- coding: utf-8 --
import scrapy
from utils.utils import *
from utils.constants import *


class SpidetSpider(scrapy.Spider):
	name = 'spidet'
	allowed_domains = [ALLOWED_DOMAIN]
	start_urls = [START_URLS]

	# Saca las urls de la web y las pone en formato valido ("https://elpais.com/" + url)
	def parse(self, response):
		urls = response.xpath(XPATH_URLS).extract()
		
		for url in urls:
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_details)
		
	# Con esta función sacamos los posibles titulos y articulos (ya que cada pagina tiene un formato diferente)
	def parse_details(self, response):
		
		t1 = response.xpath(XPATH_TITLE1).extract_first()
		t2 = response.xpath(XPATH_TITLE2).extract_first()
		t3 = response.xpath(XPATH_TITLE3).extract_first()
		t4 = response.xpath(XPATH_TITLE4).extract_first()
		t5 = response.xpath(XPATH_TITLE5).extract_first()
		t6 = response.xpath(XPATH_TITLE6).extract_first()
		t7 = response.xpath(XPATH_TITLE7).extract_first()
		t8 = response.xpath(XPATH_TITLE8).extract_first()

		c1 = response.xpath(XPATH_ART1).extract()
		c2 = response.xpath(XPATH_ART2).extract()
		c3 = response.xpath(XPATH_ART3).extract()
		c4 = response.xpath(XPATH_ART4).extract()
		c5 = response.xpath(XPATH_ART5).extract()
		c6 = response.xpath(XPATH_ART6).extract()
		c7 = response.xpath(XPATH_ART7).extract()
		c8 = response.xpath(XPATH_ART8).extract()
		c9 = response.xpath(XPATH_ART9).extract()

		list_titles = [t1,t2,t3,t4,t5,t6,t7,t8]
		list_content = [c1,c2,c3,c4,c5,c6,c7,c8,c9]

		# Llamamos a una funcion seleccionamos el articulo correcto (algunas funciones devuelmen mas de un argumento)
		content = select_art(list_content)

		# Seleccionamos el titulo correcto (algunas funciones devuelmen mas de un argumento)
		title = select_title(list_titles)
		
		#Unimos las p seleccionadas 
		content = " ".join(content)
	
		# Escribimos en nuestro fichero txt el titulo + el articulo, separados por "|"
		while open(FILE_PATH,"w") as f :
			f.write(title+"|"+content+"\n")
			yield title