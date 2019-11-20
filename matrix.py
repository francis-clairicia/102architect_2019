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
			raise ValueError()
		else:
			return object.__new__(cls)
		
	def __init__(self, lines, columns):
		self.lines = lines
		self.columns = columns
		self.mat = {}
		for i in range(lines):
			for j in range(columns):
				self.mat[i + 1, j + 1] = 0
	
	def __repr__(self):
		matrix_str = ""
		for i, j in self.mat.keys():
			matrix_str += f"{round(self.mat[i, j], 2):.2f}"
			matrix_str += "\t" if (j < self.columns) else "\n"
		return matrix_str[:-1]
		
	def __str__(self):
		"""Pareil que 'repr'"""
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
	
	def __len__(self):
		return self.lines * self.columns

	def __add__(self, matrix_added):
		if (self.lines != matrix_added.lines) or (self.columns != matrix_added.columns):
			raise ValueError("Matrix don't have the same dimensions")
		new_matrix = Matrix(self.lines, self.columns)
		for coord in self.mat.keys():
			new_matrix[coord] = self.mat[coord] + matrix_added[coord]
		return new_matrix
	
	def __iadd__(self, matrix_added):
		return self + matrix_added
	
	def __mul__(self, value):
		if (type(value) in [int, float]):
			return self.multiplicate_by_constante(value)
		matrix_mul = value
		if (self.columns != matrix_mul.lines):
			error = "Can't multiplicate {0}x{1} matrix with {2}x{3} matrix ({1} != {2})"
			raise ValueError(error.format(self.lines, self.columns, matrix_mul.lines, matrix_mul.columns))
		new_matrix = Matrix(self.lines, matrix_mul.columns)
		for n, p in new_matrix.coords():
			for i, j in zip(range(matrix_mul.lines), range(self.columns)):
				i += 1
				j += 1
				new_matrix[n, p] += matrix_mul[i, p] * self.mat[n, j]
		return new_matrix
	
	def __rmul__(self, value):
		return self * value
	
	def __imul__(self, value):
		return self * value

	def multiplicate_by_constante(self, k):
		for coord in self.mat.keys():
			self.mat[coord] *= k
		return self
	
	def coords(self):
		return self.mat.keys()
		
	def reset(self):
		for coord in self.mat.keys():
			self.mat[coord] = 0

def unit_matrix(n):
	m = Matrix(n, n)
	for i in range(1, n + 1):
		m[i, i] = 1
	return m
