#!/usr/bin/python3
INDICE_DATO = 1

class Heap:
	def __init__(self, func_cmp):
		self.lista = []
		self.cantidad = 0
		self.func_cmp = func_cmp

	def __len__(self):
		return self.cantidad
	
	def upheap(self, posicion):
		if not posicion:
			return
		padre = (posicion-1)//2
		if (self.func_cmp(self.lista[padre], self.lista[posicion])) < 0:
			self.lista[padre], self.lista[posicion] = self.lista[posicion], self.lista[padre]
			self.upheap(padre)

	def downheap(self, cantidad, posicion):
			if posicion >= cantidad:
				return
			maximo = posicion;
			izq = 2 * posicion + 1;
			der = 2 * posicion + 2;
			if izq < cantidad and self.func_cmp(self.lista[izq], self.lista[maximo]) > 0:
				maximo = izq

			if der < cantidad and self.func_cmp(self.lista[der], self.lista[maximo]) > 0:
				maximo = der

			if maximo != posicion:
				self.lista[posicion], self.lista[maximo] = self.lista[maximo], self.lista[posicion]
				self.downheap(cantidad, maximo)

	def encolar(self, dato):
		self.lista.append(dato)
		self.upheap(self.cantidad)
		self.cantidad += 1

	def esta_vacio(self):
		return self.cantidad == 0

	def ver_minimo(self):
		if(heap_esta_vacia(self)):
			return None
		return self.lista[0]

	def desencolar(self):
		if self.esta_vacio():
			raise Exception ("El Heap esta vacio")
		dato = self.lista[0]
		self.cantidad -= 1
		self.lista[0] = self.lista[self.cantidad]
		self.lista.pop(self.cantidad)
		self.downheap(self.cantidad, 0)
		return dato

	

	
	






