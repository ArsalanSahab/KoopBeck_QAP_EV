"""
ROULETTE AND TOURNAMENT SELECTION TECHNIQUES USED
SOURCE: https://www.hindawi.com/journals/mpe/2016/3672758
"""

import numpy as np
import random

# Initialization class
class Selection(object):

    def __init__(self, selection_algorithm):
        self.selection_algorithm = selection_algorithm

    def select(self, population, fitness_scores):
        return self.selection_algorithm(population, fitness_scores)

# Class for Tournament Selection implementation.
class TournamentSelection(object):

    def __init__(self):
        pass

    def __call__(self, population, fitness_score_list):
        return self.tournament_selection(population, fitness_score_list)

    # Initiate tournament selection
    @staticmethod
    def tournament_selection(population_list, fitness_scores_list, elitism=False):

        new_species = []
        # If elitisim is enabled, size is decremented by 1 to
        # promote the fittest
        population_size = len(fitness_scores_list) - 1 if elitism else len(fitness_scores_list)

        #
        for _ in range(0, population_size):

            # Take two parent indices
            parent_1 = random.randint(0, len(fitness_scores_list) - 1)
            parent_2 = random.randint(0, len(fitness_scores_list) - 1)

            # Compare scores
            # The parent with the higher fitness wins
            if fitness_scores_list[parent_1] > fitness_scores_list[parent_2]:
                ch_winner = population_list[parent_1]
            else:
                ch_winner = population_list[parent_2]

            # Add to list
            new_species.append(ch_winner)

        return new_species
