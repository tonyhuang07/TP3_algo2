INIFITO = 99999999
INDICE_PESO = 1
INDICE_ARISTA = 0
from grafo import *
from heap import *
from cola import *
from cola import *
import random


def _camino_mas(grafo, origen):
	factor = {}
	padre = {}
	for v in grafo.obtener_vertices():
		factor[v] = INIFITO

	factor[origen] = 0
	padre[origen] = None
	heap_factor = Heap(comparar_pesos) 
	heap_factor.encolar((origen,factor[origen]))
	while not heap_factor.esta_vacio():
		v = heap_factor.desencolar()[0]
		for destino in grafo.adyacentes(v):
			numero_factor = factor[v] + grafo.peso(v, destino)
			if numero_factor < factor[destino]:
				factor[destino] = numero_factor 
				padre[destino] = v
				heap_factor.encolar((destino, factor[destino]))

	return padre, factor 


def _camino_escalas(grafo, origen, destino):
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
				if w == destino:
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
			if(funcion == _camino_escalas):
				padre, factor = funcion(grafo, origen, destino)
			else:
				padre, factor = funcion(grafo, origen)

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


def nueva_aerolinea(grafo, archivo):
	grafo_minimo = prim(grafo)
	with open(archivo, "w") as f:
		rutas = grafo_minimo.obtener_aristas()
		for ruta in rutas:
			origen, destino = ruta
			linea = origen + " -> " + destino
			f.write(linea + ", ")
		print("OK")


def comparar_pesos(peso1, peso2):
	dato1 = peso1[INDICE_PESO]
	dato2 = peso2[INDICE_PESO]
	return (dato1-dato2)*(-1)

def prim(grafo):
	vertice = grafo.obtener_vertice_aleatorio()
	visitados = set()
	visitados.add(vertice)
	heap = Heap(comparar_pesos)
	for w in grafo.adyacentes(vertice):
		heap.encolar(((vertice, w), grafo.peso(vertice, w)))
	grafo_minimo = Grafo()
	while not heap.esta_vacio():
		dato = heap.desencolar()
		w = (dato[0][1])
		v = (dato[0][0])
		peso = (dato[1])
		if w in visitados:
			continue
		grafo_minimo.agregar_vertice(v)
		grafo_minimo.agregar_vertice(w)
		grafo_minimo.agregar_arista(v, w, peso)
		visitados.add(w)
		for adyacente in grafo.adyacentes(w):
			if adyacente not in visitados:
				heap.encolar(((w, adyacente), grafo.peso(w, adyacente)))
	return grafo_minimo











