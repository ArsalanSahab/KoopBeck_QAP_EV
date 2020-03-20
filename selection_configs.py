"""
ROULETTE AND TOURNAMENT SELECTION TECHNIQUES USED 

SOURCE :

https://www.hindawi.com/journals/mpe/2016/3672758

"""

#### PYTHON IMPORTS ####
import numpy as np
import random



# MAIN INITALISATION CLASS
class Selection(object):

    def __init__(self, selection_algorithm):

        self.selection_algorithm = selection_algorithm

    def select(self, population, fitness_scores):

        return self.selection_algorithm(population, fitness_scores)

# CLASS TO IMPLEMENT ROULETTE SELECTION (CODE FOR THIS CLASS HAS BEEN TAKEN FROM THE INTERNET AND EDITED)
class RouletteSelection(object):

    # IN THE ROULETTE SELECTION TECHNIQUE CHROMOSOMES WITH BETTER FITNESS ARE SELECTED MORE OFTEN

    def __init__(self):

        pass

    def __call__(self, population, fitness_score_list):

        return self.selection(population, fitness_score_list)

   # FUNCTION TO INITIATE CURRENT SELECTION PROCESS
    @staticmethod
    def selection(population, fitness_scores_list):
        new_population = []

        # Remove maximum value from every element so roulette selection will rely on bigger difference
        worst_result = np.min(fitness_scores_list)
        fitness_scores_list = list(map(lambda value: value - worst_result, fitness_scores_list))

        cumulative_sum = np.cumsum(fitness_scores_list)

        for _ in range(len(population)):
            probability_of_choose = random.uniform(0, 1) * sum(fitness_scores_list)
            randomly_selected_member = RouletteSelection.select_chromosome(population,
                                                                           cumulative_sum,
                                                                           probability_of_choose)
            new_population.append(randomly_selected_member)

        return new_population

    # FUNCTION TO SELECT CHROMOSOMES FOR THE CURRENT SELECTION TECHNIQUE
    @staticmethod
    def select_chromosome(population, cumulative_sum, randomly_generated_probability):

        for index, _ in enumerate(cumulative_sum):

            if randomly_generated_probability <= cumulative_sum[index]:

                return population[index]


# CLASS TO IMPLEMENT TOURNAMENT SELECTION (CODE FOR THIS CLASS HAS BEEN TAKEN FROM THE INTERNET AND EDITED)
class TournamentSelection(object):

    def __init__(self):

        pass

    def __call__(self, population, fitness_score_list):

        return self.tournament_selection(population, fitness_score_list)

    # FUNCTION TO INITIATE THE TOURNAMENT SELECTION ALGORITHM
    @staticmethod
    def tournament_selection(population_list, fitness_scores_list, elitism=False):

        new_species = []
        population_size = len(fitness_scores_list)
        population_size = population_size - 1 if elitism else population_size

        for _ in range(0, population_size):

            # Take best
            of_parent_idx = random.randint(0, len(fitness_scores_list) - 1)
            tf_parent_idx = random.randint(0, len(fitness_scores_list) - 1)

            if fitness_scores_list[of_parent_idx] > fitness_scores_list[tf_parent_idx]:

                ch_winner = population_list[of_parent_idx]

            else:

                ch_winner = population_list[tf_parent_idx]

            new_species.append(ch_winner)

        return new_species