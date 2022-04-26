import numpy as np
import pandas as pd
import tkinter as tk
import random
import math
import tsp_graph_init

class Ant :
	chemin = [0]
	lieux_restant = []
	STATE = 'DEFAULT' #DEFAULT LOOKING BACKTRACK PHEROMON
	current_place = (0,0)

	def action(self, graph) :
		if self.STATE == 'DEFAULT' :
			self.current_place = graph.liste_lieux[0]
			self.lieux_restant = graph.liste_lieux
			self.STATE = 'LOOKING'

		if self.STATE == 'LOOKING' :
			if len(lieux_restant) == 0 :
				self.current_place = graph.liste_lieux[0]
				self.STATE = 'BACKTRACK'
			else :
				next_place = 0
				
		if self.STATE == 'BACKTRACK' :

		if self.STATE == 'PHEROMON' :

