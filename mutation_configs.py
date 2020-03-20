#### PYTHON IMPORTS ####
import random

#### CUSTOM IMPORTS ####
from configurations import MUTATION_PERCENTAGE

# INITIATOR CLASS
class Mutation(object):

    def __init__(self, mutation_algorithm):

        self.mutation_algorithm = mutation_algorithm

    def mutate(self, population):

        return self.mutation_algorithm(population)


# MAIN CLASS TO IMPLEMENT MUTATION TECHNIQUE (SOME PARTS OF CODE FOR THIS CLASS HAVE BEEN TAKEN FROM THE INTERNET)
class BasicMutation(object):

    def __init__(self):

        pass

    def __call__(self, population):

        return self.mutate_population(population)


    # FUNCTION TO APPLY MUTATION TO WHOLE POPULATION
    @staticmethod
    def mutate_population(population):

        mutated_chromosomes = []

        for chromosome in population:

            if 0 <= random.uniform(0, 1) <= MUTATION_PERCENTAGE:

                mutated_chromosome = BasicMutation.mutate_chromosome(chromosome,
                                                                     BasicMutation.gen_rand_index(
                                                                         chromosome))
                mutated_chromosomes.append(mutated_chromosome)

            else:

                mutated_chromosomes.append(chromosome)

        return mutated_chromosomes

    # FUNCTION TO APPLY MUTATION TO CHROMOSOMES
    @staticmethod
    def mutate_chromosome(chromosome, index):

        gen_1_index, gen_2_index = index
        chromosome[gen_1_index], chromosome[gen_2_index] = chromosome[gen_2_index], chromosome[gen_1_index]

        return chromosome

    # FUNCTION TO GENERATE RANDOM INDEX FOR CHROMOSOME MUTATION
    @staticmethod
    def gen_rand_index(chromosome):

        return random.randint(0, len(chromosome) - 1), random.randint(0, len(chromosome) - 1)
