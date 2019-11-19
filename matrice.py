# -*- coding:Utf-8 -*
##
## EPITECH PROJECT, 2019
## 102architect_2019
## File description:
## matrice.py
##

"""
Ce module contient une classe permettant
de créer et de manipuler des matrices
"""

class Matrice(object):
	
	def __new__(cls, ligne, colonne):
		if ligne <= 0 or colonne <= 0:
			raise ValueError("Les valeurs sont innappropriées")
		else:
			return object.__new__(cls)
		
	def __init__(self, ligne, colonne):
		self.ligne = ligne
		self.colonne = colonne
		
		# Pour cela, on va utiliser un dictionnaire
		self.mat = {}
		for i in range(ligne):
			for j in range(colonne):
				self.mat[i, j] = 0
	
	def __repr__(self):
		"""Représentation de la matrice dans la console"""
		
		nbre_max = 8 #Nbre de chiffres max affichées dans la grille
		
		assert nbre_max > 0
		
		n = nbre_max + 1
		
		# D'abord la numérotation des colonnes
		matrice = "    "
		for i in range(self.colonne):
			numero_de_colonne = str(i)
			for k in range(n-2):
				matrice += " "
				k += 1
			if len(numero_de_colonne) == 1:
				matrice += " "
			matrice += numero_de_colonne
		# On va à la ligne
		matrice += "\n"
		# Ensuite la ligne du tableau du dessus
		matrice += "   +"
		for i in range(self.colonne):
			for k in range(n):
				matrice += "-"
		matrice += "-+"
		# On va à la ligne
		matrice += "\n"
		# Et maintenant affichage de chaque ligne de la matrice
		for i in range(self.ligne):
			numero_de_ligne = str(i)
			matrice += " "
			if len(numero_de_ligne) == 1:
				matrice += " " 
			matrice += numero_de_ligne + "|"
			for j in range(self.colonne):
				valeur = str(self.mat[i ,j])
				espace = ""
				for l in range(nbre_max,0,-1):
					espace += " "
					if l == len(valeur):
						break
				matrice += espace + valeur
			matrice += " |"
			# On va à la ligne
			matrice += "\n"
		# Fermer le tableau
		matrice += "   +"
		for i in range(self.colonne):
			for k in range(n):
				matrice += "-"
		matrice += "-+"
		
		#Affichage
		return matrice
		
	def __str__(self):
		"""Pareil que 'repr'"""
		return repr(self)
		
	def __getitem__(self, coord):
		"""Retourne la valeur des coordonnées de la matrice"""
		
		if coord in self.mat.keys():
			return self.mat[coord]
		else:
			raise KeyError("Coordonées non trouvé")
			
	def __setitem__(self, coord, valeur):
		"""Modifie une valeur de la matrice"""
		
		if coord in self.mat.keys():
			self.mat[coord] = valeur
		else:
			raise KeyError("Coordonées non trouvé")
	
	def __delitem__(self, coord):
		"""Va mettre la valeur de la matrice à 0"""
		if coord in self.mat.keys():
			self.mat[coord] = 0
		else:
			raise KeyError("Coordonées non trouvé")
	
	def __len__(self):
		print(self.ligne, "lignes")
		print(self.colonne, "colonnes")
		return len(self.mat)
			
	def coords(self):
		return self.mat.keys()
		
	def reset(self):
		for coord in self.mat.keys():
			self.mat[coord] = 0