# -- coding: utf-8 --
import scrapy

	# Coge la lista de diccionarios y saca la mayor longitud
	def maximo(list_content):
		l_len = []
		for d in list_content:
			l_len.append(d["len"])
		max_d = max(l_len)
		return max_d

	# Esta funcion pasa los articulos admitidos y los pasa a una lista de diccionarios con el articulo y su longitud. 
	# Maximo(). Saca el articulo acorde a la longitud maxima
	def get_art_mayor(list_content):
		list_len = []
		for art in list_content:
			d = {"len" :len(str(art)), "art":art}
			list_len.append(d)
		max_d = maximo(list_len)
		final_content = (item for item in list_len if item["len"] == max_d).next()
		return final_content

	# Esta funcion comprueba que los titulos no esten vacios, o erroneos para sacar el valido
	def select_title(list_titles):
		final_title = "Título no encontrado"
		for title in list_titles:
			if title != "" and title is not None and title != "\n":
				final_title = title

		return final_title.encode("utf-8")

	# Esta funcion selecciona el o los articulos que no estan vacios, luego llama a otra funcion para seleccionar el valido y lo devuelve
	def select_art(list_content):
		final_content = "Contenido no encontrado"
		accepted = []
		for content in list_content:
			if content != "" and content is not None:
				accepted.append(content)
		final_content = get_art_mayor(accepted)
		return final_content["art"].encode("utf-8")