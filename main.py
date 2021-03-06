"""
NOTE : SOME PARTS OF CODE IN THIS PROJECT HAVE BEEN INSPIRED FROM
"Filip Bachura from Wroclaw University of Science and Technology"
"""
import sys
import os.path
import time
import numpy as np
import time
import random


print("Starting ....")

# Add current path to the system PATH to import local files
sys.path.append(os.path.join(os.path.dirname(__file__), ''))

from configurations import POPULATION_SIZE, NUMBER_OF_GENERATIONS,DATA_SET, SLEEP_TIME
from load_data_set import array_size, flow_array, distance_array
from fitness_func_configs import normalise_fitness_scores, get_fitness_scores
from selection_configs import TournamentSelection
from crossover_configs import Crossover
from mutation_configs import Mutation
from turtle_drawer import TurtleDrawer
from Graphs.plot_drawer import PlotDrawer



# Selection strategies from imported using the initialization functions
selection_strategy = TournamentSelection()
# CrossOver strategies from imported using the initialization functions
crossover_strategy = Crossover()
# Mutation strategies from imported using the initialization functions
mutation_strategy = Mutation()

def main():
    # Generate random population of chromosomes
    population = [] # Chromosomes are appended in this

    for i in range(POPULATION_SIZE):
        # Every chromosome is a list of numbers
        chromosome = list(range(array_size))
        # ...randomized/shuffled.
        random.shuffle(chromosome)
        # Add to population
        population.append(chromosome)


    turtle_drawer = TurtleDrawer()
    plot_drawer = PlotDrawer()

    # Result arrays for plotting
    generation_indices = []
    average_results = []
    min_results = []
    max_results = []

    # Keep track of the last max_chromosome to avoid redundancy
    previous_max_chromosome = []


    for gen_count in range(NUMBER_OF_GENERATIONS):
        # Calculate fitness from distance and flow using imported function
        fitness_scores = get_fitness_scores(population, distance_array, flow_array)
        # Normalize fitness score by inverting and dividing by the total
        fitness_scores_normalized = normalise_fitness_scores(fitness_scores)

        # While it's not normalized yet, max is the worst, therefore min is the most suitable
        # Use numpy to get min, max, and average
        max_fitness = np.min(fitness_scores)
        min_fitness = np.max(fitness_scores)
        average_fitness = np.mean(fitness_scores)
        max_chromosome = population[np.argmin(fitness_scores)]
        max_chromosome = list(map(lambda value: value + 1, max_chromosome))

        # Use the imported strategy functions to select chromosomes from
        # population based on the normalized scores
        selected_chromosomes = selection_strategy.start_tournament(population, fitness_scores_normalized)

        # Input the selected chromosomes to the imported crossover function
        crossed_chromosomes = crossover_strategy.start_crossover(selected_chromosomes)
        # Apply mutation over the crossever chromosomes
        mutated_chromosomes = mutation_strategy.start_mutation(crossed_chromosomes)


        # Print current values to the terminal
        print("Generation_Count: \t\t\t\t{}\nMean fitness.: \t\t\t{}\nMax score: \t\t\t{}\nMax chromosome.: \t\t{}\n\n"
              .format(gen_count, average_fitness, max_fitness, max_chromosome))


        # DRAWING FRAME

        # Implementing the turtle functions and iteratively drawing
        def draw_visual_frame():
        # The function takes flow and distance arrays, the best chromosome,
        # and other data and draws points and lines representing flow and distance
            turtle_drawer.draw_main_frame(
                    max_chromosome, gen_count, max_fitness,
                    max_chromosome, flow_array, distance_array
                    )

            # Delay between each iteration of drawing
            time.sleep(SLEEP_TIME)

            return


        if previous_max_chromosome != max_chromosome :

            draw_visual_frame()


        # Update the max chromosome
        previous_max_chromosome = max_chromosome

        # Update the population to the one generated by the mutation strategy
        population = crossed_chromosomes

        # For plot drawing
        # ----------------
        # Add fitness scores to the results arrays, to be used in plot drawing
        max_results.append(max_fitness)
        min_results.append(min_fitness)
        average_results.append(average_fitness)
        # Add an increment to the generation indices, for the x-axis of the plot
        generation_indices.append(gen_count)

        # wait for 2 seconds between consective output generation
        # time.sleep(2)

        # Draw and save a plot at the first generation, and every 1/5ths of the total generations after that,
        # and then at the very last generation.
        if gen_count == 0 or gen_count % (NUMBER_OF_GENERATIONS / 5) == 0 or gen_count == NUMBER_OF_GENERATIONS - 1:
            plot_drawer.drawPlot("Plot_For_" + 'Gen_' + str(gen_count), generation_indices, average_results, max_results, min_results, path='Graphs')

       # turtle_drawer.screen.mainloop()



if __name__ == "__main__":
    main()



