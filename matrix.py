# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## matrice.py
##

class Matrix(object):
	
	def __new__(cls, lines, columns):
		if lines <= 0 or columns <= 0:
			raise ValueError("Dimensions not valid")
		else:
			return object.__new__(cls)
		
	def __init__(self, lines, columns):
		self.lines = lines
		self.columns = columns
		self.mat = {}
		for i in range(1, lines + 1):
			for j in range(1, columns + 1):
				self.mat[i, j] = 0

	@classmethod
	def from_2d_list(cls, list_2d):
		total_columns = 0
		for line in list_2d:
			c = len(line)
			if total_columns == 0:
				total_columns = c
			elif c != total_columns:
				raise ValueError("Columns don't have the same length")
		m = cls(len(list_2d), total_columns)
		for i, j in m.coords():
			m[i, j] = list_2d[i - 1][j - 1]
		return m

	@classmethod
	def unit(cls, n):
		m = cls(n, n)
		for i in range(1, n + 1):
			m[i, i] = 1
		return m

	def __repr__(self):
		matrix_str = ""
		for i, j in self.mat.keys():
			value = round(self.mat[i, j], 2)
			if (value == 0):
				value = 0
			matrix_str += f"{value:.2f}"
			matrix_str += "\t" if (j < self.columns) else "\n"
		return matrix_str[:-1]
		
	def __str__(self):
		return repr(self)

	def __getitem__(self, coord):
		if coord in self.mat.keys():
			return self.mat[coord]
		else:
			raise KeyError("Coords not found")

	def __setitem__(self, coord, valeur):
		if coord in self.mat.keys():
			self.mat[coord] = valeur
		else:
			raise KeyError("Coords not found")
	
	def __delitem__(self, coord):
		if coord in self.mat.keys():
			self.mat[coord] = 0
		else:
			raise KeyError("Coords not found")

	def __add__(self, matrix_added):
		if (type(matrix_added) is not Matrix):
			raise TypeError("Cannot matrix and {}".format(type(matrix_added)))
		if (self.lines != matrix_added.lines) or (self.columns != matrix_added.columns):
			raise ValueError("Matrix don't have the same dimensions")
		new_matrix = Matrix(self.lines, self.columns)
		for coord in self.mat.keys():
			new_matrix[coord] = self.mat[coord] + matrix_added[coord]
		return new_matrix
	
	def __iadd__(self, matrix_added):
		if (type(matrix_added) is not Matrix):
			raise TypeError("Cannot matrix and {}".format(type(matrix_added)))
		if (self.lines != matrix_added.lines) or (self.columns != matrix_added.columns):
			raise ValueError("Matrix don't have the same dimensions")
		for coord in self.mat.keys():
			self.mat[coord] += matrix_added[coord]
		return self
	
	def __mul__(self, value):
		if (type(value) in [int, float]):
			return self.multiplicate_by_constante(value)
		if (type(value) is not Matrix):
			raise TypeError("Cannot multiplicate matrix and {}".format(type(value)))
		matrix_mul = value
		if (self.columns != matrix_mul.lines):
			error = "Can't multiplicate {0}x{1} matrix with {2}x{3} matrix ({1} != {2})"
			raise ValueError(error.format(self.lines, self.columns, matrix_mul.lines, matrix_mul.columns))
		new_matrix = Matrix(self.lines, matrix_mul.columns)
		for n, p in new_matrix.coords():
			for i, j in zip(range(1, matrix_mul.lines + 1), range(1, self.columns + 1)):
				new_matrix[n, p] += matrix_mul[i, p] * self.mat[n, j]
		return new_matrix
	
	def __rmul__(self, value):
		if type(value) in [int, float]:
			return self.multiplicate_by_constante(value)
		raise TypeError("Cannot multiplicate {} and matrix".format(type(value)))
	
	def __imul__(self, value):
		if (type(value) in [int, float]):
			return self.multiplicate_by_constante(value)
		if (type(value) is not Matrix):
			raise TypeError("Cannot multiplicate matrix and {}".format(type(value)))
		matrix_mul = value
		if (self.columns != matrix_mul.lines):
			error = "Can't multiplicate {0}x{1} matrix with {2}x{3} matrix ({1} != {2})"
			raise ValueError(error.format(self.lines, self.columns, matrix_mul.lines, matrix_mul.columns))
		new_matrix = Matrix(self.lines, matrix_mul.columns)
		for n, p in new_matrix.coords():
			for i, j in zip(range(1, matrix_mul.lines + 1), range(1, self.columns + 1)):
				new_matrix[n, p] += matrix_mul[i, p] * self.mat[n, j]
		self.mat = dict(new_matrix.mat)
		return self

	def multiplicate_by_constante(self, k):
		for coord in self.mat.keys():
			self.mat[coord] *= k
		return self
	
	def coords(self):
		return self.mat.keys()
		
	def reset(self):
		for coord in self.mat.keys():
			self.mat[coord] = 0
