INIFITO = 99999999



class Vuelo:

	def __init__(self, origen, destino, tiempo, precio, cantidad):
		self.origen = origen
		self.destino = destino
		self.tiempo = tiempo
		self.precio = precio
		self.cantidad = cantidad

	def obtener_origen(self)
		return self.origen

	def obtener_destino(self)
		return self.destino

	def obtener_tiempo(self)
		return self.tiempo

	def obtener_precio(self)
		return self.precio

	def obtener_cantidad(self)
		return self.cantidad

class v:

	def __init__(self, ciudad, codigo, latitud, longitud):
		self.ciudad = ciudad
		self.codigo = codigo
		self.latitud = latitud
		self.longitud = longitud

	def obtener_ciudad(self)
		return self.ciudad

	def obtener_codigo(self)
		return self.codigo

	def obtener_latitud(self)
		return self.latitud

	def obtener_longitud(self)
		return self.longitud


def camino_mas(grafo, origen):
	factor = {}
	padre = {}
	for v in grafo.obtener_vertices(): #falta la funcion
		factor[v] = INIFITO

	factor[origen] = 0
	padre[origen] = None
	heap_factor = heap() #falta la clase heap
	heap_factor.encolar(origen,factor[origen])
	while not heap_factor.esta_vacia():
		v = heap_factor.desencolar()
		for distino in grafo.adyacentes(v):
			numero_factor = factor[v] + grafo.peso(v,distino)
			if numero_factor < factor[distino]:
				factor[distino] = fnumero_factor 
				padre[distino] = v
				heap_factor.encolar(distino, factor[distino])

	return padre, factor 


def camino_escalas(grafo, origen, distino):
	vistados = set()
	padre = {}
	orden = {}
	padre[origen] = None
	orden [origen] = 0
	pila_aero = pila()
	pila_aero.apilar(origen)
	while not pila_aero.esta_vacia():
		v = pila_aero.desapilar()
		for w in grafo.adyacentes(v):
			if w not in vistados:
				padre[w] = v
				orden[w] = orden[v] + 1
				if w = distino:
					break

				pila_aero.apilar(w)

	return padre, orden







