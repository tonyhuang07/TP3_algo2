import sys
from grafo import *
import biblioteca
"""
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
"""
INDICE_CIUDAD = 0
INDICE_AEROPUERTO = 1
INDICE_LATITUD = 2 
INDICE_LONGITUD = 3

def cargar_aeropuertos(f):
	ciudades = {}
	aeropuertos = {}
	with open(f, "r") as f:
		for linea in f:
			campos = linea.strip().split(",")
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
CANTIDAD_PESOS = 3
GRAFO_TIEMPO = 0
GRAFO_PRECIO = 1
GRAFO_CANTIDAD = 2

def cargar_vuelos(f, grafos):
	for i in range(CANTIDAD_PESOS):
		nuevo_grafo = Grafo()
		grafos.append(nuevo_grafo)
	with open(f, "r") as f:
		for linea in f:
			campos = linea.strip().split(",")
			indice_peso = INDICE_TIEMPO
			for grafo in grafos:
				grafo.agregar_vertice(campos[INDICE_ORIGEN])
				grafo.agregar_vertice(campos[INDICE_DESTINO])
				grafo.agregar_arista(campos[INDICE_ORIGEN], campos[INDICE_DESTINO], int(campos[indice_peso]))
				indice_peso+=1

def eliminar_espacio(linea):
	instruccion = ""
	for i in range(len(linea)):
		if (linea[i] == " "):
			instruccion+=","
			break;
		instruccion+=linea[i]
	instruccion+=linea[i+1:]
	return instruccion

def main():
	if (len(sys.argv) == 1 or len(sys.argv) > 3):
		print("Cantidad de parametros incorrecta")
		return
	ciudades, aeropuertos = cargar_aeropuertos(sys.argv[1])
	grafos = []
	cargar_vuelos(sys.argv[2], grafos)
	for linea in sys.stdin:
		instruccion = eliminar_espacio(linea)
		campos = instruccion.rstrip().split(",")
		comando = campos[0]
		cantidad_parametros = len(campos)-1
		print(campos)
		
		if (comando == "listar_operaciones"):
			biblioteca.listar_operaciones()

		elif (comando == "camino_mas" and cantidad_parametros == 3):
			if (campos[1] == "rapido"):
				biblioteca.camino_mas(grafos[GRAFO_TIEMPO], campos[2], campos[3], ciudades)
			elif (campos[1] == "barato"):
				biblioteca.camino_mas(grafos[GRAFO_PRECIO], campos[2], campos[3], ciudades)
			else:
				print("Error en comando camino_mas")

		elif (comando == "camino_escalas" and cantidad_parametros == 2):
			biblioteca.camino_escalas(grafo[GRAFO_TIEMPO], campos[1], campos[2])

		elif (comando == "centralidad" and cantidad_parametros == 1):
			biblioteca.centralidad(grafo[GRAFO_CANTIDAD], campos[1])

		else:
			print("Error en comando")
		
		
main()





