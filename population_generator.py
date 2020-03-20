#### PYTHON IMPORTS ####
import random

# Generate random population
def generate_population(num_selected, num_chromosomes):
    population = [] # Chromosomes are appended in this

    for i in range(num_chromosomes):
        chromosome = list(range(num_selected))
        random.shuffle(chromosome)
        population.append(chromosome)

    return population
