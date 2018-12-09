#!/usr/bin/python3
class Nodo:

	def __init__(self,dato):
		self.dato = dato
		self.proxi = None



class Cola:

	def __init__(self):
		self.primero = None
		self.ultimo = None

	def encolar(self,dato):
			if not self.primero:
				self.primero = Nodo(dato)
				self.ultimo = self.primero
				return
			self.ultimo.proxi = Nodo(dato)
			self.ultimo = self.ultimo.proxi
	def desencolar(self):

		if not self.primero:
			raise ValueError("La cola esta vacia")

		dato = self.primero.dato
		self.primero = self.primero.proxi
		return dato

	def esta_vacia(self):
		return self.primero == None



def intercalar(colas):
	resul = Cola()
	todas_vacias = False
	while not todas_vacias:
		estan_todas_vacias = True
		for cola in colas:
			if not cola.esta_vacia():
				resul.encolar(cola.desencolar())
				estan_todas_vacias = False
	return resul