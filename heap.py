FACTOR = 1

class Heap_minimo:
	def __init__(self):
		self.lista = []
		self.cantidad = 0

	def __len__(self):
		return self.cantidad

	def heap_encolar(self, dato):
		self.lista[self.cantidad] = dato
		self.upheap(self.lista, self.cantidad)
		self.cantidad +=1

	def heap_esta_vacia(self):
		return self.cantidad ==0

	def heap_ver_minimo(self):
		if(heap_esta_vacia(self)):
			return None
		return self.lista[0]

	def heap_desencolar(self):
		if heap_esta_vacia(self):
			raise Exception ('heap esta vacia')


		dato = self.lista[0]
		self.cantidad -=1
		self.lista[0] = self.lista[self.cantidad]
		self.downheap(self.lista, self.cantidad, 0)
		return dato

	def heapify(arreglo, n):
		for i in range (n/2, 1, -1):
			self.downheap(arreglo, n, i-1)

	def upheap(arreglo, posicion):
		if not posicion:
			return
		padre = (posicion - 1)/2
		if(arreglo[padre][FACTOR] < arreglo[posicion][FACTOR]):
			arreglo[padre], arreglo[posicion] = arreglo[posicion], arreglo[padre]
			upheap(arreglo, padre)

	def downheap(arreglo, cantidad, posicion):
		if posicion >=canttidad:
			return
		minimo = posicion;
		izq = 2 * posicion + 1;
		der = 2 * posicion + 2;
		if izq < cant and arreglo[izq][FACTOR] > arreglo[minomo][FACTOR]:
			minimo = izq

		if der < cant and arreglo[der][FACTOR] > arreglo[minomo][FACTOR]:
			minimo = der

		if minimo != posicion:
			arreglo[posicion], arreglo[minimo] = arreglo[minomo], arreglo[posicion]
			downheap(arreglo, cantidad, minimo)






