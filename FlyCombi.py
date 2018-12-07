import grafo
import funciones_auxiliares

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

class Aeropuerto:

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

INDICE_CIUDAD = 0
INDICE_AEROPUERTO = 1
INDICE_LATITUD = 2 
INDICE_LONGITUD = 3

def cargar_aeropuertos(f):
	ciudades = {}
	aeropuertos = {}
	with open(f, "r") as f:
		for linea in f:
			campos = line.strip().split(",")
			ciudad, codigo_aeropuerto = campos[INDICE_CIUDAD], campos[INDICE_AEROPUERTO]
			aeropuertos_ciudad = ciudades.get(ciudad, [])
			aeropuertos_ciudad.append(codigo_aeropuerto)
			ciudades[ciudad] = aeropuertos_ciudad
			aeropuertos[codigo_aeropuerto] = campos
	return ciudades, aeropuertos

INDICE_ORIGEN = 0
INDICE_DESTINO = 1
INDICE_TIEMPO = 2
INDICE_PRECIO = 3
INDICE_CANTIDAD_VUELOS = 4
CANTIDAD_GRAFOS = 3
GRAFO1 = 

def cargar_vuelos(f):
	grafos = []
	for i in range(CANTIDAD_GRAFOS)
		grafos.append(Grafo())
	with open(f, "r") as f:
		for linea in f:
			campos = line.strip().split(",")
			indice_peso = INDICE_TIEMPO
			for grafo in grafos:
				grafo.crear_vertice(campos[INDICE_ORIGEN])
				grafo.crear_vertice(campos[INDICE_DESTINO])
				grafo.crear_arista(campos[INDICE_ORIGEN], campos[INDICE_DESTINO], campos[indice_peso])
				indice_peso++;
	return grafos
			
					
"""Verificar casos base de recepcion de parametros invalidos"""

def main():

	







