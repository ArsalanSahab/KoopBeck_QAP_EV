#### PYTHON IMPORTS ####
import random


# FUNCTION TO GENERATE RANDOM POPULATION

def generate_population(num_selected, num_chromosomes):

    population = []

    for i in range(num_chromosomes):

        chromosome = list(range(num_selected))
        random.shuffle(chromosome)
        population.append(chromosome)

    return population
