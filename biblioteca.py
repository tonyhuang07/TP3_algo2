INIFITO = 99999999
from grafo import *
from heap import *
from cola import *
from cola import *
import random



# class Vuelo:

# 	def __init__(self, origen, destino, tiempo, precio, cantidad):
# 		self.origen = origen
# 		self.destino = destino
# 		self.tiempo = tiempo
# 		self.precio = precio
# 		self.cantidad = cantidad

# 	def obtener_origen(self)
# 		return self.origen

# 	def obtener_destino(self)
# 		return self.destino

# 	def obtener_tiempo(self)
# 		return self.tiempo

# 	def obtener_precio(self)
# 		return self.precio

# 	def obtener_cantidad(self)
# 		return self.cantidad

# class v:

# 	def __init__(self, ciudad, codigo, latitud, longitud):
# 		self.ciudad = ciudad
# 		self.codigo = codigo
# 		self.latitud = latitud
# 		self.longitud = longitud

# 	def obtener_ciudad(self)
# 		return self.ciudad

# 	def obtener_codigo(self)
# 		return self.codigo

# 	def obtener_latitud(self)
# 		return self.latitud

# 	def obtener_longitud(self)
# 		return self.longitud


def _camino_mas(grafo, origen):
	factor = {}
	padre = {}
	for v in grafo.obtener_vertices(): #falta la funcion
		factor[v] = INIFITO

	factor[origen] = 0
	padre[origen] = None
	heap_factor = Heap_minimo() 
	heap_factor.encolar((origen,factor[origen]))
	while not heap_factor.esta_vacia():
		v = heap_factor.desencolar()[0]
		for distino in grafo.adyacentes(v):
			numero_factor = factor[v] + grafo.peso(v, distino)
			if numero_factor < factor[distino]:
				factor[distino] = numero_factor 
				padre[distino] = v
				heap_factor.encolar((distino, factor[distino]))

	return padre, factor 


def _camino_escalas(grafo, origen, distino):
	vistados = set()
	padre = {}
	orden = {}
	padre[origen] = None
	orden [origen] = 0
	cola_aero = Cola()
	cola_aero.encolar(origen)
	while not cola_aero.esta_vacia():
		v = cola_aero.desencolar()
		for w in grafo.adyacentes(v):

			if w not in vistados:
				vistados.add(w)
				padre[w] = v
				orden[w] = orden[v] + 1
				if w == distino:
					break

				cola_aero.encolar(w)

	return padre, orden

def _centralidad (grafo):
	cent = {}
	for v in grafo:
		cent[v] = 0
	for v in grafo:
		padre, frecuencia = camimo_mas(grafo, v)
		cent_aux = {}

		for w in grafo:
			cent_aux[w] = 0;
			vertices_ordenados = ordenar_vertices (grafo, frecuencia) #funcion ordenar filtrar los vertices infinitos

		for w in vertices_ordenados:
			cent_aux[padre[w]] += 1 + cen_aux[w]

		for w in grafo:
			if w == v:
				continue
			cent[w] += cent_aux[w]

		return cent

def ordenar_vertice (grafo, factor):
	vertice_ordenados = list(factor)
	for v in vertice_ordenados:
		if factor[v] == INIFITO:
			vertice_ordenados.remove(v)

	vertice_ordenados.sort(key=lambda x: factor[x], reverse=True)

	return vertice_ordenados


def vertices_aleatorios(pesos):
    total = sum(pesos.values())
    rand = random.uniform(0, total)
    acum = 0
    for vertice, peso_arista in pesos.items():
        if acum + peso_arista >= rand:
            return vertice
        acum += peso_arista

def _centralidad_aprox(grafo):
	cent = {}
	for v in grafo:
		cent[v] = 0

	for v in grafo:
		pesos = {}
		for w in grafo.adyacentes(v):
			pesos[w] = grafo.obtener_peso(v,w);
		vertice = vertices_aleatorios(pesos)
		cent[vertice] += 1

	return cent



def camino_mas(grafo, ciudad_origen, ciudad_destino, ciudades):

	return imprimir_camino(_camino_mas, grafo, ciudad_origen, ciudad_destino, ciudades)


	# caminos_minimos = {}

	# for origen in ciudades[ciudad_origen]:
	# 	print(origen)
	# 	for destino in ciudades[ciudad_destino]:
	# 		padre, factor = _camino_mas(grafo, origen)
	# 		vuelos = []
	# 		aero_actual = destino
	# 		while aero_actual != origen:
	# 			vuelos.append(aero_actual)
	# 			aero_actual = padre[aero_actual]

	# 		vuelos.append(origen)

	# 		caminos_minimos[vuelos] = factor[destino]

	# caminos = list(caminos_minimos)
	# caminos.sort(key = lambda x: caminos_minimos[x])
	# resultado = " -> ".join(caminos[0][::-1])
	# print(resultado)
def camino_escalas(grafo, ciudad_origen, ciudad_destino, ciudades):

	return imprimir_camino(_camino_escalas, grafo, ciudad_origen, ciudad_destino, ciudades)


def imprimir_camino(funcion, grafo, ciudad_origen, ciudad_destino, ciudades):
	menor_factor = INIFITO
	lista_ciudades = []
	for origen in ciudades[ciudad_origen]:
		for destino in ciudades[ciudad_destino]:
			padre, factor = funcion(grafo, origen, destino)

			sub_lista = []
			aero_actual = destino
			while aero_actual != origen:
				sub_lista.append(aero_actual)
				aero_actual = padre[aero_actual]

			sub_lista.append(origen)
			
			if factor[destino] < menor_factor:
				lista_ciudades = sub_lista
				menor_factor = factor[destino] 


	resultado= " -> ".join(lista_ciudades[::-1])
	print(resultado)


def centralidad(grafo,n):
	return imprimir_centralidad(_centralidad, grafo, n)


def centralidad_aprox(grafo,n):
	return imprimir_centralidad(_centralidad_aprox, grafo, n)

def imprimir_centralidad(funcion, grafo, n):
	dic = funcion(grafo)
	lista = list(resultado)
	lista.sort(key = lambda x: dic[x],reverse = True)
	resultado = ", ".join(lista[0:n])
	print(resultado)















