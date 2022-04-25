import numpy as np
import tkinter as tk
import pandas as pd
import random
import time
import math


class Lieu :
	"""class describing a place"""
	def __init__(self, x, y) :
		self.x = x
		self.y = y

	def calcul_distance(self, l2) :
		return math.sqrt((self.x - l2.x)**2 + (self.y - l2.y)**2)


l1 = Lieu(1,2)
l2 = Lieu(2,3)

print(l1.calcul_distance(l2))

class Graph :
	"""class describing a graph"""
	LARGEUR = 800
	HAUTEUR = 600
	NB_LIEU = 10

	def __init__(self) :
		self.liste_lieux = []
		for i in range (self.NB_LIEU) :
			x = random.randint(0, self.LARGEUR)
			y = random.randint(0, self.HAUTEUR)
			self.liste_lieux.append(Lieu(x, y))

	def calcul_matrice_cout_od(self) :
		mat = np.zeros((self.NB_LIEU, self.NB_LIEU))
		for i in range(self.NB_LIEU) :
			for j in range(self.NB_LIEU) :
				mat[i][j] = self.liste_lieux[i].calcul_distance(self.liste_lieux[j])
		return mat

g1 = Graph()
print(g1.calcul_matrice_cout_od())