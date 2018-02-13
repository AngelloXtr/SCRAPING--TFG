# -- coding: utf-8 --

# Fichero sobre el que volcaremos los resultados de la araña

FILE_PATH = 'output.txt'


# Constantes utilizadas por la araña

ALLOWED_DOMAIN = 'elpais.com'
START_URLS = 'https://elpais.com/'


# XPaths utilizados para recorrer las urls de la página

XPATH_URLS = '//section[starts-with(@class, "bloque_")]/div/div/div/article/div/h2[@class="articulo-titulo"]/a/@href'


# XPaths utilizados para la extracción del contenido relacionado con los títulos

XPATH_TITLE1 = '//*[@id="articulo-titulo"]/text()'
XPATH_TITLE2 = '//*[@id="titulo_noticia"]/text()'
XPATH_TITLE3 = '//*[@id="entry-title"]/text()'
XPATH_TITLE4 = '//*[@class="titulo_noticia"]/text()'
XPATH_TITLE5 = '//*[@class="entry-title"]/text()'
XPATH_TITLE6 = '//div[@class="titular cf"]/h1/text()'
XPATH_TITLE7 = '//*[@class="articulo-titulo"]/text()'
XPATH_TITLE8 = '//div[@class="single-title"]/div/h1/text()'


# XPaths utilizados para la extracción del contenido relacionado con los artículos

XPATH_ART1 = '//*[@class="articulo-cuerpo"]/p[not(@class="siguenos_opinion")]/text()'
XPATH_ART2 = '//div[@class="row texto shareable"]/div/div/text()'
XPATH_ART3 = '//*[@itemprop="articleBody"]/p[not(@class="siguenos_opinion")]/text()'
XPATH_ART4 = '//*[starts-with(@class, "entry-content")]/p/text()'
XPATH_ART5 = '//div[@class="post-contents"]/p/text()'
XPATH_ART6 = '//*[@class="texto-galeria"]/p/text()'
XPATH_ART7 = '//p[@dir="ltr"]/text()'
XPATH_ART8 = '//*[@class="foto-texto"]/text()' 
XPATH_ART9 = '//div[@class="entradilla"]/p/text()'