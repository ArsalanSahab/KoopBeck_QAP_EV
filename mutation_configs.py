import random

from configurations import MUTATION_PERCENTAGE

# Initiator class
class Mutation(object):

    def __init__(self, mutation_algorithm):
        self.mutation_algorithm = mutation_algorithm

    def mutate(self, population):
        return self.mutation_algorithm(population)


# Main class for mutation (SOME PARTS OF CODE FOR THIS CLASS HAVE BEEN TAKEN FROM THE INTERNET)
class BasicMutation(object):

    def __init__(self):
        pass

    def __call__(self, population):
        return self.mutate_population(population)


    # Apply mutation to whole population
    @staticmethod
    def mutate_population(population):

        mutated_chromosomes = []

        for chromosome in population:

            # Mutate a chromosome if a randomly drawn sample is between
            # 0 and the specified threshold
            if 0 <= random.uniform(0, 1) <= MUTATION_PERCENTAGE:

                # Input chromosome and random index to static function
                # to mutate the single chromosome
                mutated_chromosome = BasicMutation.mutate_chromosome(
                        chromosome,
                        BasicMutation.gen_rand_index(chromosome)
                )
                # Add the mutated chromosome to the list
                mutated_chromosomes.append(mutated_chromosome)

            else:
                # Add the unmutated chromosome to the list
                # in case the random sample does not satisfy
                # the criteria
                mutated_chromosomes.append(chromosome)

        return mutated_chromosomes

    # Input a chromosome and an index tuple
    # mutate/swap the given indices in the chromosome and return
    @staticmethod
    def mutate_chromosome(chromosome, index):

        gen_1_index, gen_2_index = index
        # Swap members at given indices
        chromosome[gen_1_index], chromosome[gen_2_index] = chromosome[gen_2_index], chromosome[gen_1_index]

        return chromosome

    # Input chromosome, generate 2-tuple of random indices
    @staticmethod
    def gen_rand_index(chromosome):

        return random.randint(0, len(chromosome) - 1), random.randint(0, len(chromosome) - 1)
