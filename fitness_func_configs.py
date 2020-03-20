
#### PYTHON IMPORTS ####
import numpy as np

# FUNCTION TO COMPUTE THE FITNESS SCORES
def get_fitness_scores(population, distance_array, flow_array):

    array_size = distance_array.shape[0]
    fitness_scores = []

    for chromosome in population:

        assert len(chromosome) == len(set(chromosome))

        chromosome_fitness_sum = 0

        for x in range(array_size):

            for y in range(array_size):

                chromosome_fitness_sum += distance_array[x, y] * flow_array[chromosome[x] - 1, chromosome[y] - 1]

        fitness_scores.append(chromosome_fitness_sum)

    return fitness_scores

# FUNCTION TO NORMALISE FITNESS SCORES (SOME PART OF CODE TAKEN FROM INTERNET NUMPY DOCUMENTATION)
def normalise_fitness_scores(fitness_scores):

    map_to_minimization_problem = list(map(lambda value: 1. / value, fitness_scores))
    normalized_scores = np.array(map_to_minimization_problem) / np.sum(map_to_minimization_problem)

    return normalized_scores
