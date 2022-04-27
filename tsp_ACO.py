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
	lieux_restant = []
	STATE = 'DEFAULT' #DEFAULT LOOKING BACKTRACK PHEROMON
	current_place = tgi.Lieu(0,0)

	def action(self, graph) :
		if self.STATE == 'DEFAULT' :
			self.chemin = []
			self.dist_parcour = 0
			self.current_place = graph.liste_lieux[0]
			self.lieux_restant = graph.liste_lieux
			self.STATE = 'LOOKING'

		if self.STATE == 'LOOKING' :
			# make the ant go through the graph
			if len(self.lieux_restant) == 0 :
				self.current_place = graph.liste_lieux[0]
				self.STATE = 'BACKTRACK'
			else :
				next_place = 0
				dist_min = 1000
				prob_next = []
				for i in range(len(lieux_restant)) :
					#decision making to know which place to visit next
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