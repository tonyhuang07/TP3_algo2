FACTOR = 1

class Heap_minimo:
	def __init__(self):
		self.lista = []
		self.cantidad = 0

	def __len__(self):
		return self.cantidad

	def encolar(self, dato):
		self.lista.append(dato)
		self.upheap(self.lista,self.cantidad)
		self.cantidad +=1

	def esta_vacia(self):
		return self.cantidad ==0

	def ver_minimo(self):
		if(self.esta_vacia()):
			return None
		return self.lista[0]

	def desencolar(self):
		if self.esta_vacia():
			raise Exception ('heap esta vacia')


		dato = self.lista[0]
		self.cantidad -=1
		self.lista[0] = self.lista[self.cantidad]
		self.downheap(self.lista, self.cantidad, 0)
		return dato

	def heapify(self,arreglo, n):
		for i in range (n/2, 1, -1):
			self.downheap(arreglo, n, i-1)

	def upheap(self,arreglo, posicion):
		if not posicion:
			return
		padre = int((posicion - 1)/2)
		if(arreglo[padre] < arreglo[posicion]):
			arreglo[padre], arreglo[posicion] = arreglo[posicion], arreglo[padre]
			self.upheap(arreglo, padre)

	def downheap(self,arreglo, cantidad, posicion):
		if posicion >=cantidad:
			return
		minimo = posicion;
		izq = 2 * posicion + 1;
		der = 2 * posicion + 2;
		if izq < cantidad and arreglo[izq] > arreglo[minimo]:
			minimo = izq

		if der < cantidad and arreglo[der]> arreglo[minimo]:
			minimo = der

		if minimo != posicion:
			arreglo[posicion], arreglo[minimo] = arreglo[minimo], arreglo[posicion]
			self.downheap(arreglo, cantidad, minimo)






