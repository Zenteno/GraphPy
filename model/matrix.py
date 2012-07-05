import copy	# Para hacer copias superficiales (shallow copies)

class Matrix:
	"""Clase que maneja la Matriz de Adyacencia/Incidencia"""
	
	def __init__(self, dim):
		self.__dimMatrix = dim
		self.__matrix = self.__set_matrix(dim)
	
	#
	#  PRIVATE METHODS
	#
	
	def __set_matrix(self, dim):
		"""Para una dimension "dim":
		Crea una nueva matriz. Todos sus elementos tienen el valor '0'
		Retorna la nueva matriz"""
		matrix = []
		for i in range(dim):
			matrix.append([])
			for j in range(dim):
				matrix[i].append(0)
		return matrix
	
	#
	#  PUBLIC METHODS
	#
	
	def get_dim(self):
		"""Retorna una copia 'superficial' (por valor) de la dimension"""
		dim = copy.copy(self.__dimMatrix)
		return dim
	
	def get_matrix(self):
		"""Retorna una copia 'superficial' (por valor) de la matriz"""
		matrix = copy.copy(self.__matrix)
		return matrix
	
	def add_entry(self):
		"""Agrega los datos de un nodo (nueva fila y columna)
		Retorna la nueva dimension de la matriz"""
		try:
			new = []
			for i in range(self.__dimMatrix):
				new.append(0)
			self.__matrix.append(new)
			self.__dimMatrix += 1
			for i in range(self.__dimMatrix):
				self.__matrix[i].append(0)
		except:
			return False
		return True
	
	def del_entry(self, target):
		"""Para un indice "target":
		Elimina los datos de un nodo (fila & columna respectiva)
		Retorna la nueva dimension de la matriz"""
		try:
			self.__matrix.pop(target)
			for i in range(self.__dimMatrix - 1):
				self.__matrix[i].pop(target)
			self.__dimMatrix -= 1
		except:
			return False
		return True
	
	def set_relation(self, row, col, value):
		"""Inserta un valor en el elemento (row, col) de la matriz"""
		self.__matrix[row][col] = value
	
	def symmetry(self):
		"""Determina si la matriz es simetrica o no
		Retorna 'True' si es simetrica, 'False' si no lo es"""
		dim = self.__dimMatrix
		for i in range(dim):
			for j in range(dim):
				if j <= i:
					continue
				if self.__matrix[i][j] != self.__matrix[j][i]:
					return False
		return True
	
	def num_relations(self, entry):
		dim = self.__dimMatrix
		relations = 0
		for i in range(dim):
			if self.__matrix[entry][i] != 0:
				relations += 1
		return relations