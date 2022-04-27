import numpy as np
import pandas as pd
import tkinter as tk
import random
import math
import tsp_graph_init as tgi

class Ant :
	"""class describing an ant used to go throught a graph and to determine the optimal way throught it""" 
	chemin = [0]
	dist_parcour = 0
	lieux_restant = [] #contient les indices des lieux non visité dans graph.liste_lieux
	STATE = 'DEFAULT' #DEFAULT LOOKING BACKTRACK PHEROMON
	current_place = -1 #indice correspondant au noeud dans graph.liste_lieux

	def action(self, graph) :
		if self.STATE == 'DEFAULT' :
			self.chemin = []
			self.dist_parcour = 0
			self.current_place = 0
			self.lieux_restant = graph.liste_lieux

			self.STATE = 'LOOKING'

		if self.STATE == 'LOOKING' :
			# make the ant go through the graph
			if len(self.lieux_restant) == 0 :
				self.current_place = 0
				self.STATE = 'BACKTRACK'
			else :
				next_place = 0
				dist_min = 1000
				prob_next = []
				for i in range(len(lieux_restant)) :
					#decision making to know which place to visit next
					'''
					proba = 1
					proba = proba/(self.current_place.calcul_distance(self.lieux_restant[i]))
					proba = proba*self.lieux_restant[i].phero
					r = random.uniform(0, 1)
					prob_next.append(proba*r)
				max_prob = prob_next[0]
				c = 0
				for i in range(len(prob_next)) :
					if max_prob < prob_next[i] :
						max_prob = prob_next[i]
						c = i
				next_place = self.lieux_restant[c]
				self.current_place = next_place
				self.chemin.append(self.current_place)
				del self.lieux_restant[c]
				'''
				#matrice des phéromones pour l'instant attribut du graphe p-e à changer dans le futur si on la passe en paramètre (donc la retourne dans le mode PHEROMON) ou la mettre en variable global (je prefererai éviter) ou trouver un anbalogue aux pointeurs du C mais en python
				mat_pheromone = graph.mat_phero

				mat_dist = graph.calcul_matrice_cout_od()

				proba_lieu_restant = []
				#calcul des proba de chaques destination
				mat_proba = np.ones(mat_pheromone.shape)
				mat_proba = np.multiply(mat_proba, mat_pheromone)
				mat_proba = np.multiply(mat_proba, np.recirocal(mat_dist))

				for i in range(len(mat_proba[self.current_place])) :
					#sélection des lieux non visité uniquement
					if i in lieux_restant :
						r = random.uniform(0, 1)
						#ajout du facteur random pour le choix (potentiellement à changer je ne sais pas si c'est la bonne méthod ou les bonnes valeurs)
						proba_lieu_restant.append((i, mat_proba[self.current_place][i]*r))
				#tri des proba des lieux restant pour savoir sur lequel on va
				proba_lieu_restant = proba_lieu_restant.sort(key=lambda y: y[1])
				next_place = proba_lieu_restant[0][0]
				self.current_place = next_place
				#suppression du lieu dans la liste des lieux restant
				del lieux_restant[proba_lieu_restant[0][0]]


		if self.STATE == 'BACKTRACK' :
			#the ant has reached its destination
			self.current_place = graph.liste_lieux[0]
			self.STATE =  'PHEROMON'

		if self.STATE == 'PHEROMON' :
			#the ant plant pheromon on the way it took 
			for i in range(len(self.chemin)) :
				self.current_place.phero += 0.01
				self.current_place = self.chemin[len(self.chemin)-i]
			for i in range(len(self.chemin) - 1) :
				self.dist_parcour += self.chemin[i].calcul_distance(self.chemin[i+1])
			result = (self.chemin, self.dist_parcour)
			self.STATE = 'DEFAULT'

## TODO add randomness to next place selection ##

## changement sur les phéromones, pour l'instant sur les sommets, à mettre sur les arêtes ##