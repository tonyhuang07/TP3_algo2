#!/usr/bin/python3
class Grafo:
	def __init__(self):
		self.aristas = {}
		self.peso_total = 0

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
		self.aristas[origen].append((destino, peso))

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
