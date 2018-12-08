class Grafo:
	def __init__(self):
		self.aristas = {}

	def agregar_vertice(self, dato):
		if dato in self.aristas:
			return
		self.aristas[dato] = []

	def agregar_arista(self, origen, destino, peso):
		if (destino, peso) in self.aristas[origen]:
			return
		self.aristas[origen].append((destino, peso))

	def obtener_adyacentes(self, vertice):
		adyacentes = []
		for destino, peso in self.aristas[vertice]:
			adyacentes.append(destino)

		return adyacentes

	def ver_conexiones(self):
		for vertice in self.aristas:
			print("\n {} tiene de adyacentes a: [{}]".format(vertice, self.aristas[vertice]))
'''
	def obtener_peso_arista(self, origen, destino)
		return self.aristas[origen][destino]
'''
'''
class Arista:
	def __init__(self, origen, destino, peso)
		self.origen = origen
		self.destino = destino
		self.peso = peso

class Vertice:
	def __init__(self, dato):
		self.dato = dato

	def obtener_dato(self):
		return self.dato
'''
