"""
NOTE : SOME PARTS OF CODE IN THIS PROJECT HAVE BEEN INSPIRED FROM 
"Filip Bachura from Wroclaw University of Science and Technology"

"""



##### IMPORTS PYTHON ####

import sys
import os.path
import time
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), ''))

#### CUSTOM IMPORTS ####


from configurations import POPULATION_SIZE, NUMBER_OF_GENERATIONS, DRAW_VISUALIZATION, DATA_SET, DRAW_GRAPH
from load_data_set import array_size, flow_array, distance_array
from population_generator import generate_population
from fitness_func_configs import normalise_fitness_scores, get_fitness_scores
from selection_configs import Selection, TournamentSelection, RouletteSelection
from crossover_configs import BasicCrossover, Crossover
from mutation_configs import Mutation, BasicMutation
from turtle_visualisations import CustomDrawer
from draw_plot import PlotDrawer

# STRATEGIES SELECTION
selection_strategy = Selection(selection_algorithm=TournamentSelection())
mutation_strategy = Mutation(mutation_algorithm=BasicMutation())
crossover_strategy = Crossover(crossover_algorithm=BasicCrossover())

# MAIN METHOD
def main():

    population = generate_population(array_size, POPULATION_SIZE)

    turtle_drawer = CustomDrawer()
    plot_drawer = PlotDrawer()

    generation_indicies = []
    average_results = []
    min_results = []
    max_results = []
    previous_max_chromosome = []

    def draw_visual_frame():

        turtle_drawer.draw_main_frame(max_chromosome, gen_count, max_fitness, max_chromosome, flow_array,
                                                   distance_array)

        time.sleep(1)

        return

    def terminal_output():

        print("Generation_Count: \t\t\t\t{}\nMean fitness.: \t\t\t{}\nMax score: \t\t\t{}\nMax chromosome.: \t\t{}\n\n"
              .format(gen_count, average_fitness, max_fitness, max_chromosome))

    for gen_count in range(NUMBER_OF_GENERATIONS):

        fitness_scores = get_fitness_scores(population, distance_array, flow_array)
        fitness_scores_normalized = normalise_fitness_scores(fitness_scores)

        # While it's not normalized yet, max means "the worst", therefor "min" for us.
        max_fitness = np.min(fitness_scores)
        min_fitness = np.max(fitness_scores)
        average_fitness = np.mean(fitness_scores)

        max_results.append(max_fitness)
        min_results.append(min_fitness)
        average_results.append(average_fitness)
        generation_indicies.append(gen_count)

        max_chromosome = population[np.argmin(fitness_scores)]
        max_chromosome = list(map(lambda value: value + 1, max_chromosome))

        selected_chromosomes = selection_strategy.select(population, fitness_scores_normalized)
        crossed_chromosomes = crossover_strategy.crossover(selected_chromosomes)
        mutated_chromosomes = mutation_strategy.mutate(crossed_chromosomes)

        terminal_output()
        if DRAW_VISUALIZATION and previous_max_chromosome != max_chromosome:
            draw_visual_frame()

        previous_max_chromosome = max_chromosome

        population = mutated_chromosomes

    if DRAW_GRAPH:

        plot_drawer.drawPlot(DATA_SET, generation_indicies, average_results, max_results, min_results)

    turtle_drawer.screen.mainloop()


if __name__ == "__main__":
    main()



