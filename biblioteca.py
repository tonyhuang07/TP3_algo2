#!/usr/bin/python3
INIFITO = 99999999
INDICE_PESO = 1
INDICE_ARISTA = 0
from grafo import *
from heap import *
from cola import *
from cola import *
import random

def listar_operaciones():
	print("camino_mas")
	print("camino_escalas")
	#print("centralidad")
	print("centralidad_aprox")
	print("nueva_aerolinea")
	print("vacaciones")

def _camino_mas(grafo, origen, frecuencia):
	factor = {}
	padre = {}
	for v in grafo.obtener_vertices():
		factor[v] = INIFITO

	factor[origen] = 0
	padre[origen] = None
	if frecuencia:
		heap_factor = Heap(_comparar_pesos)
	else:
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

def _centralidad(grafo):
	# cent = {}
	# for v in grafo.obtener_vertices(): 
	# 	cent[v] = 0
	# for v in grafo.obtener_vertices():
	# 	for w in grafo.obtener_vertices():
	# 		if v == w or grafo.esta_conectado(v,w):
	# 			continue
	# 		padre, frecuencia = _camino_mas(grafo, v, 1)
			
	# 		if not padre[w] : 
	# 			continue 
			
	# 		actual = padre[w]

	# 		while actual != v:
	# 			cent[actual] += 1
	# 			actual = padre[actual]

	# return cent

	cent = {}

	for v in grafo.obtener_vertices():
		cent[v] = 0

	for v in grafo.obtener_vertices():
		padre, distancia = _camino_mas(grafo, v, 1)
		cent_aux = {}

		for w in grafo.obtener_vertices():
			cent_aux[w] = 0	
		vertices_ordenados = ordenar_vertices(grafo, distancia)

		for w in vertices_ordenados:
			if w == v:
				continue
			cent_aux[padre[w]] += 1 
			cent_aux[padre[w]] += cent_aux[w]

		for w in grafo.obtener_vertices():
			if w == v:
				continue
			cent[w] += cent_aux[w]

	return cent

def ordenar_vertices(grafo, factor):
	vertices_ordenados = list(factor)

	vertices_ordenados.sort(key=lambda x: factor[x], reverse=True)

	vertice_actual = vertices_ordenados[0]

	while factor[vertice_actual] == INIFITO:
		vertices_ordenados.pop(0)
		vertice_actual = vertices_ordenados[0]

	return vertices_ordenados


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
	for v in grafo.obtener_vertices():
		cent[v] = 0

	for v in grafo.obtener_vertices():
		pesos = {}
		for w in grafo.adyacentes(v):
			pesos[w] = grafo.peso(v,w);
		vertice = vertices_aleatorios(pesos)
		if vertice:
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
				padre, factor = funcion(grafo, origen, 0)

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
	lista = list(dic)
	lista.sort(key = lambda x: dic[x],reverse = True)
	resultado = ", ".join(lista[0:int(n)])
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

def _comparar_pesos(peso1, peso2):
	dato1 = peso1[INDICE_DATO]
	dato2 = peso2[INDICE_DATO]
	return (dato1-dato2)


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

def _vacaciones(grafo, origen, n, ciudades, visitados, aeros_abandonados):
	for aero in ciudades[origen]:
		visitados[aero] = n
		for v in grafo.adyacentes(aero):
			visitados[v] = n - 1
			if hay_recorrido(grafo, aero, v, visitados, aeros_abandonados, n-1):
				return True

		del visitados[aero]

	return False
	#print("no hay recorrido")



def hay_recorrido(grafo, origen, vertice, visitados, aeros_abandonados, n):
	if n==1:
		if origen in grafo.adyacentes(vertice):
			return True
		else:
			del visitados[vertice]
			aeros_abandonados_n = aeros_abandonados[n]
			aeros_abandonados_n.append(vertice)
			aeros_abandonados[n] = aeros_abandonados_n
			return False

	for w in grafo.adyacentes(vertice):
		#print("\nAeropuertos abandonados: \n\n")
		#print(aeros_abandonados)
		if w not in visitados and  w not in aeros_abandonados[n-1]:
			visitados[w] = n-1
			if hay_recorrido(grafo, origen, w, visitados, aeros_abandonados, n-1):
				return True
	del visitados[vertice]
	aeros_abandonados_n = aeros_abandonados[n]
	aeros_abandonados_n.append(vertice)
	aeros_abandonados[n] = aeros_abandonados_n
	return False

def vacaciones(grafo, origen, n, ciudades):

	visitados = {}
	aeros_abandonados = {}
	for i in range (n):
		aeros_abandonados[i+1] = []

	if _vacaciones(grafo, origen, n, ciudades, visitados, aeros_abandonados):
		lista = list(visitados)
		lista.sort(key = lambda x: visitados[x],reverse = True)
		lista.append(lista[0])
		print(" -> ".join(lista))


	else:
		print("No hay recorrido")

"""
def hay_recorrido(grafo, origen, vertice, visitados, aeros_abandonados, n):
	if (n==1):
		if origen in grafo.adyacentes(vertice):
			return True
		else:


	for w in grafo.adyacentes(vertice):
		visitados[w]=

"""






