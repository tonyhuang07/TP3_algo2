#!/usr/bin/python3

#########################################
# Algoritmos y Programación II - TP3	#
#										#
# Corrector: Buchwald, Martín			#
#										#
# Alumnos:	 Huang, Yuhong				#
#			 Klein, Santiago			#
#										# 
#########################################


class Grafo:
	def __init__(self, es_no_dirigido):
		self.aristas = {}
		self.peso_total = 0
		self.es_no_dirigido = es_no_dirigido

	def __len__(self):
		return len(self.aristas)

	def agregar_vertice(self, dato):
		if dato in self.aristas:
			return
		self.aristas[dato] = []

	def agregar_arista(self, origen, destino, peso):
		if (destino, peso) in self.aristas[origen]:
			return
		self.peso_total += peso
		aristas_origen = self.aristas[origen]
		aristas_origen.append((destino, peso))
		self.aristas[origen] = aristas_origen
		if self.es_no_dirigido:
			aristas_destino = self.aristas[destino]
			aristas_destino.append((origen, peso))
			self.aristas[destino] = aristas_destino

	def adyacentes(self, vertice):
		adyacentes = []
		for destino, peso in self.aristas[vertice]:
			adyacentes.append(destino)
		return adyacentes

	def pertenece(self, vertice):
		return (vertice in self.aristas)

	def obtener_aristas(self):
		aristas_totales = []
		for origen in self.aristas:
			for destino, peso in self.aristas[origen]:
				aristas_totales.append((origen, destino))
		return aristas_totales


	def ver_conexiones(self):
		for vertice in self.aristas:
			print("\n {} tiene de adyacentes a: [{}]".format(vertice, self.aristas[vertice]))

	def obtener_vertices(self):
		return list(self.aristas)

	def peso(self, origen, destino):
		for tupla in self.aristas[origen]:
			if tupla[0] == destino:
				return tupla[1]

	def obtener_peso_total(self):
		return self.peso_total

	def obtener_vertice_aleatorio(self):
		return list(self.aristas)[0]
