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
	mat_phero = np.ones((NB_LIEU, NB_LIEU))


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
mat_dist = g1.calcul_matrice_cout_od()

class Route :
	"""class describing the road followed to go through every place on the graph once and back to the beginning"""
	ordre = [0]

	def calcul_distance_route(self) : 
		dt = 0
		for i in range(len(self.ordre) - 1) :
			dt += self.ordre[i].calcul_distance(self.ordre[i+1])
		return dt

class Affichage :
	LARGEUR = 800
	HAUTEUR = 600
	@classmethod
	def crea_fenetre(cls):
		cls.root = tk.Tk()
		cls.root.title("IA Spatial - Maina, Nathan, Hervé, Quentin")
		cls.root.geometry("1200x700")
		cls.root.bind("<Escape>", lambda x: cls.root.destroy())
		cls.canva = tk.Canvas(cls.root, scrollregion=(0,0,500,500), height=cls.HAUTEUR, width=cls.LARGEUR)  
		cls.canva.pack(expand=True)
		cls.lab_text = tk.StringVar()
		cls.lab_text.set("Ant n°0")
		cls.lab = tk.Label(cls.root, textvariable=cls.lab_text, fg="#715ec1")
		cls.lab.pack(expand="True")
		tk.mainloop()

	
    
canv = Affichage()
canv.crea_fenetre()

