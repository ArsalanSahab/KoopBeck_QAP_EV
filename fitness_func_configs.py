import numpy as np

'''
Input Population, Distance, and Flow Arrays, compute fitness scores
from distance array and flow array. The flow is given by the indices
at the corresponding coordinates from the chromosomes. The scores
from all chromosomes are added, later to be normalized.
'''
def get_fitness_scores(population, distance_array, flow_array):

    array_size = distance_array.shape[0]
    fitness_scores = []

    for chromosome in population:
        # Make sure there are no duplicates in chromosome
        assert len(chromosome) == len(set(chromosome))

        # Initialize sum
        chromosome_fitness_sum = 0

        # At each (x, y) the distance is given by the distance array
        # and the flow for each item given by the chromosome are
        # multiplied to get the fitness.
        # This is done for all chromosomes in the population.
        for x in range(array_size):
            for y in range(array_size):
                chromosome_fitness_sum += distance_array[x, y] * flow_array[chromosome[x] - 1, chromosome[y] - 1]

        # Add calculated sum to the scores array
        fitness_scores.append(chromosome_fitness_sum)

    return fitness_scores

# NORMALISE FITNESS SCORES (SOME PART OF CODE TAKEN FROM INTERNET NUMPY DOCUMENTATION)
def normalise_fitness_scores(fitness_scores):

    # Generate list of inverses from fitness_scores
    map_to_minimization_problem = list(map(lambda value: 1.0 / value, fitness_scores))
    # Normalizes each score by dividing it by the total
    normalized_scores = np.array(map_to_minimization_problem) / np.sum(map_to_minimization_problem)

    return normalized_scores
