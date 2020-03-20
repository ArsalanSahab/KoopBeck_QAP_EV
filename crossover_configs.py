#### PYTHON IMPORTS ####
import copy
import random

#### CUSTOM IMPORTS ####

from configurations import CROSSOVER_PERCENTAGE


# INITIATOR CLASS

class Crossover(object):
    def __init__(self, crossover_algorithm):

        self.crossover_algorithm = crossover_algorithm

    def crossover(self, population):

        return self.crossover_algorithm(population)

# MAIN CROSSOVER IMPLEMENTATION CLASS

class BasicCrossover(object):

    def __init__(self):

        pass

    def __call__(self, population):

        return self.crossover_init(population)



    # FUNCTION TO INITIATE CROSSOVER TECHNIQUE

    @staticmethod
    def crossover_init(population):

        not_crossovered = []
        to_crossover = []

        BasicCrossover.select_chromosomes(population, not_crossovered, to_crossover)

        crossover_tuples = BasicCrossover.create_crossover_tuples(not_crossovered, to_crossover)

        crossovered_species = BasicCrossover.crossover_population_iter_iter(crossover_tuples)

        return crossovered_species + not_crossovered



    # FUNCTION TO ITERATE CURRENT POPULATION FOR CROSSOVER
    @staticmethod
    def crossover_population_iter(crossover_tuples):

        crossovered = []

        for crossover_tuple in crossover_tuples:
            child_1, child_2 = BasicCrossover.chromosomes_crossover_init(
                crossover_tuple,
                # random point selected for crossover
                point_of_crossover=random.randint(0, len(crossover_tuple) - 1)
            )
            crossovered.append(child_1)
            crossovered.append(child_2)

        return crossovered

    # FUNCTION TO SELECT CHROMOSOMES
    @staticmethod
    def select_chromosomes(population, not_crossovered, to_crossover):

        for chromosome in population:

            if random.uniform(0, 1) < CROSSOVER_PERCENTAGE:

                to_crossover.append(chromosome)

            else:

                not_crossovered.append(chromosome)

    #FUNCTION TO CREATE TUPLES FROM SELECTED CHROMOSOMES FOR CROSSOVER
    @staticmethod
    def create_crossover_tuples(not_crossovered, to_crossover):

        crossover_tuples = []

        to_crossover = list(enumerate(to_crossover))

        while to_crossover:

            chromosome_to_crossover_index, chromosome_to_crossover = to_crossover.pop()

            if not to_crossover:

                not_crossovered.append(chromosome_to_crossover)

                break

            crossover_buddy_index, crossover_buddy = random.choice(to_crossover)
            to_crossover = list(filter(lambda value: value[0] != crossover_buddy_index, to_crossover))
            crossover_tuples.append((chromosome_to_crossover, crossover_buddy))

        return crossover_tuples

    # FUNCTION TO PERFORM CROSSOVER TECHNIQUE ON SELECTED CHROMOSOMES
    @staticmethod
    def chromosomes_crossover_init(parents, point_of_crossover):

        #initialise parents
        father, mother = parents

        child_1, child_2 = copy.copy(father), copy.copy(mother)

        # Change chromosome
        for index in range(point_of_crossover):

            # Values on index
            value_a = child_1[index]
            value_b = child_2[index]

            # Values for swap
            index_of_value_b_in_a = child_1.index(value_b)
            index_of_value_a_in_b = child_2.index(value_a)

        
            child_1[index_of_value_b_in_a] = value_a
            child_2[index_of_value_a_in_b] = value_b

            # Change values
            child_1[index] = value_b
            child_2[index] = value_a
            
        return child_1, child_2