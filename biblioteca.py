#!/usr/bin/python3
INIFITO = 99999999
INDICE_PESO = 1
INDICE_ARISTA = 0
CANTIDAD_VERTICE = 300
INDICE_ORIGEN = 0
INDICE_DESTINO = 1
INDICE_TIEMPO = 2
INDICE_PRECIO = 3
INDICE_CANTIDAD_VUELOS = 4
from grafo import *
from heap import *
from cola import *
from pila import *
import random

def listar_operaciones():
	print("camino_mas")
	print("camino_escalas")
	print("vacaciones")
	print("centralidad_aprox")
	print("nueva_aerolinea")
	print("centralidad")
	print("itinerario")
	print("recorrer_mundo_aprox")
	

def _camino_mas(grafo, origen, es_centralidad):
	factor = {}
	padres = {}
	for v in grafo.obtener_vertices():
		factor[v] = INIFITO

	factor[origen] = 0
	padres[origen] = None
	heap_factor = Heap(comparar_pesos) 
	heap_factor.encolar((origen,factor[origen]))
	while not heap_factor.esta_vacio():
		v = heap_factor.desencolar()[0]
		for destino in grafo.adyacentes(v):
			if (es_centralidad):
				numero_factor = factor[v] + 1/(grafo.peso(v, destino))
			else:
				numero_factor = factor[v] + grafo.peso(v, destino)
			if numero_factor < factor[destino]:
				factor[destino] = numero_factor 
				padres[destino] = v
				heap_factor.encolar((destino, factor[destino]))

	return padres, factor 


def _camino_escalas(grafo, origen, destino):
	vistados = set()
	padres = {}
	orden = {}
	padres[origen] = None
	orden[origen] = 0
	cola_aero = Cola()

	cola_aero.encolar(origen)
	while not cola_aero.esta_vacia():
		v = cola_aero.desencolar()
		for w in grafo.adyacentes(v):

			if w not in vistados:
				vistados.add(w)
				padres[w] = v
				orden[w] = orden[v] + 1
				if w == destino:
					break

				cola_aero.encolar(w)

	return padres, orden

def _centralidad(grafo):

	cent = {}
	vertices = grafo.obtener_vertices()

	for v in vertices:
		cent[v] = 0

	for v in vertices:
		padres, distancia = _camino_mas(grafo, v, True)
		cent_aux = {}

		for w in vertices:
			cent_aux[w] = 0	
		vertices_ordenados = ordenar_vertices(grafo, distancia)


		for w in vertices_ordenados:
			if w == v:
				continue
			cent_aux[padres[w]] += 1 
			cent_aux[padres[w]] += cent_aux[w]

		for w in vertices:
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

	for i in range (CANTIDAD_VERTICE):
		for v in grafo.obtener_vertices():
			pesos = {}
			for w in grafo.adyacentes(v):
				pesos[w] = grafo.peso(v,w);
			vertice = vertices_aleatorios(pesos)
			if vertice:
				cent[vertice] += 1

	return cent



def camino_mas(grafo, ciudad_origen, ciudad_destino, ciudades):
	print(" -> ".join(obtener_camino(_camino_mas, grafo, ciudad_origen, ciudad_destino, ciudades)))


def camino_escalas(grafo, ciudad_origen, ciudad_destino, ciudades):
	print(" -> ".join(obtener_camino(_camino_escalas, grafo, ciudad_origen, ciudad_destino, ciudades)))


def obtener_camino(funcion, grafo, ciudad_origen, ciudad_destino, ciudades):
	menor_factor = INIFITO
	lista_ciudades = []
	for origen in ciudades[ciudad_origen]:
		for destino in ciudades[ciudad_destino]:
			if(funcion == _camino_escalas):
				padre, factor = funcion(grafo, origen, destino)
			else:
				padre, factor = funcion(grafo, origen, False)

			sub_lista = []
			aero_actual = destino
			while aero_actual != origen:
				sub_lista.append(aero_actual)
				aero_actual = padre[aero_actual]

			sub_lista.append(origen)
			
			if factor[destino] < menor_factor:
				lista_ciudades = sub_lista
				menor_factor = factor[destino] 


	return lista_ciudades[::-1]



def centralidad(grafo,n):
	return imprimir_centralidad(_centralidad, grafo, n)


def centralidad_aprox(grafo,n):
	return imprimir_centralidad(_centralidad_aprox, grafo, n)

def imprimir_centralidad(funcion, grafo, n):
	dic = funcion(grafo)
	lista = []
	heap = Heap(comparar_pesos)
	indice = 1
	for aero in dic:
		if indice <= int(n):
			heap.encolar((aero, dic[aero]))
			indice += 1
		else:
		
			heap.encolar((aero,dic[aero]))
			heap.desencolar()
	while not heap.esta_vacio():
		(_aero, peso) = heap.desencolar()
		lista.append(_aero)
	resultado = ", ".join(lista[::-1])
	print(resultado)


def nueva_aerolinea(grafo, archivo, vuelos):
	grafo_minimo = prim(grafo)
	#if(len(grafo_minimo)==len(grafo)):
 		#print("La longitud es correcta...")
	#print("El peso total del nuevo grafo es: ",grafo_minimo.obtener_peso_total())

	with open(archivo, "w") as f:
		rutas = grafo_minimo.obtener_aristas()
		for ruta in rutas:
			info_vuelo = vuelos[ruta]
			linea = [ruta[INDICE_ORIGEN], ruta[INDICE_DESTINO], \
			 info_vuelo[INDICE_TIEMPO], info_vuelo[INDICE_PRECIO], info_vuelo[INDICE_CANTIDAD_VUELOS]]
			linea = ",".join(linea)
			f.write(linea + "\n")
		print("OK")


def comparar_pesos(peso1, peso2):
	dato1 = peso1[INDICE_PESO]
	dato2 = peso2[INDICE_PESO]
	#print("VUELOS: ", peso1, peso2, "PRECIO:", peso1[INDICE_DATO], peso2[INDICE_DATO])
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
	grafo_minimo = Grafo(True)
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


def _vacaciones(grafo, origen, n, ciudades, visitados, aeros_abadonados):
	todo_visitado = True
	for aero in ciudades[origen]:
		visitados[aero] = n


		for v in grafo.adyacentes(aero):
			visitados[v] = n - 1
			if hay_recorrido(grafo, aero,v,visitados,aeros_abadonados,n-1,todo_visitado):
				return True

		del visitados[aero]

	return False



def hay_recorrido(grafo,origen,vertice,visitados, aeros_abadonados, n, todo_visitado):
	if n == 1 :
		if origen in grafo.adyacentes(vertice):
			return True
		else:
			del visitados[vertice]

			aeros_abadonados[n].append(vertice)
			return False

	for w in grafo.adyacentes(vertice):
		if w not in aeros_abadonados[n-1]:
			todo_visitado = False

		if not w in visitados and w not in aeros_abadonados[n-1]:
			visitados[w] = n - 1
			if hay_recorrido(grafo, origen, w, visitados, aeros_abadonados, n-1, todo_visitado):
				return True
			


	del visitados[vertice]
	if todo_visitado:
		aeros_abadonados[n].append(vertice)

	return False

def vacaciones(grafo, origen, n, ciudades):
	visitados = {}
	aeros_abadonados = {}
	for i in range (n):
		aeros_abadonados[i+1] = []


	if _vacaciones(grafo, origen, n, ciudades, visitados, aeros_abadonados):
		lista = list(visitados)
		lista.sort(key = lambda x: visitados[x],reverse = True)
		lista.append(lista[0])
		print(" -> ".join(lista))


	else:
		print("No se encontro recorrido")

def _orden_topologico(grafo, v, pila, visitados):
	visitados.add(v)
	for w in grafo.adyacentes(v):
		if w not in visitados:
			_orden_topologico(grafo, w, pila, visitados)
	pila.apilar(v)

def transformar_pila_a_lista(pila):
	lista = []
	while not pila.esta_vacia():
		lista.append(pila.desapilar())
	return lista

def orden_topologico(grafo):
	visitados = set()
	pila = Pila()
	for v in grafo.obtener_vertices():
		if v not in visitados:
			_orden_topologico(grafo, v, pila, visitados)
	return transformar_pila_a_lista(pila)

def itinerario(grafo, archivo, aeropuertos_ciudades):
	grafo_orden = Grafo(False)
	with open(archivo, 'r') as f:
		linea = f.readline()
		ciudades = linea.rstrip().split(",")
		for ciudad in ciudades:
			grafo_orden.agregar_vertice(ciudad)
		for linea in f:
			orden = linea.rstrip().split(",")
			if not grafo_orden.pertenece(orden[0]):
				grafo_orden.agregar_vertice(orden[0])
			if not grafo_orden.pertenece(orden[1]):
				grafo_orden.agregar_vertice(orden[1])
			grafo_orden.agregar_arista(orden[0], orden[1], 0)
	ciudades_ordenadas = orden_topologico(grafo_orden)
	print(", ".join(ciudades_ordenadas))
	for i in range(len(ciudades)-1):
		camino_mas(grafo, ciudades_ordenadas[i], ciudades_ordenadas[i+1], aeropuertos_ciudades)



def recorrer_mundo_aprox(grafo, origen, ciudades, aeropuertos):
	ciudad_actual = origen
	visitados = set()
	lista = []
	aero = ciudades[origen][0]
	visitados.add(aero)
	lista.append(aero)
	costo = 0
	for aero in aeropuertos:
		if aero in visitados:
			continue
		visitados.add(aero)
		sub_lista = obtener_camino(_camino_mas, grafo, ciudad_actual, aeropuertos[aero][0], ciudades)

		for i in range(len(sub_lista)-1):
			visitados.add(sub_lista[i])
			costo += grafo.peso(sub_lista[i],sub_lista[i+1])

		del sub_lista[0]
		lista.extend(sub_lista)
		ciudad_actual = aeropuertos[aero][0]

	print(" -> ".join(lista))
	print("Costo: {}".format(costo))



