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

# Class for implementing Roulette Selection (PART OF THE CODE HAS BEEN TAKEN FROM THE INTERNET AND EDITED)
# In roulette selection, chromosomes with better fitness are selected more often
class RouletteSelection(object):

    def __init__(self):
        pass

    def __call__(self, population, fitness_score_list):
        return self.selection(population, fitness_score_list)

    # Initiate current selection process
    @staticmethod
    def selection(population, fitness_scores_list):
        # List for population after selection
        new_population = []

        # Remove maximum value from every element so roulette selection will rely on bigger difference
        worst_result = np.min(fitness_scores_list)
        fitness_scores_list = list(map(lambda value: value - worst_result, fitness_scores_list))

        # Sum of fitness scores
        cumulative_sum = np.cumsum(fitness_scores_list)

        #
        for _ in range(len(population)):

            # Probability is a random percentage of the sum of fitness scores
            selection_probability = random.uniform(0, 1) * sum(fitness_scores_list)

            # Select chromosome from population using a static local function
            selected_member = RouletteSelection.select_chromosome(  population,
                                                                    cumulative_sum,
                                                                    selection_probability)

            # Add to list
            new_population.append(selected_member)

        return new_population

    # Select chromosome from population based on given probability
    @staticmethod
    def select_chromosome(population, cumulative_sum, probability):

        for index, _ in enumerate(cumulative_sum):
            # Select only the chromosome at whose position the cumulative
            # sum is over the given probability
            if probability <= cumulative_sum[index]:
                return population[index]


# Class for Tournament Selection implementation (PART OF THE CODE HAS BEEN TAKEN FROM THE INTERNET AND EDITED)
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
