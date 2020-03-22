#### PYTHON IMPORTS ####
import random

# Generate random population of chromosomes
def generate_population(num_selected, num_chromosomes):
    population = [] # Chromosomes are appended in this

    for i in range(num_chromosomes):
        # Every chromosome is a list of numbers
        chromosome = list(range(num_selected))
        # ...randomized/shuffled.
        random.shuffle(chromosome)
        # Add to population
        population.append(chromosome)

    return population
