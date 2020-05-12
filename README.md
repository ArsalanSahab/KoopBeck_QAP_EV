# KoopBeck_QAP_EV
Koopmans-Beckmann Quadratic Assignment Problem Minimisation Through Evolutionary Algorithm


=======

## Problem Definition

The quadratic assignment problem was introduced by Koopmans and Beckman in 1957 . The objectives of the problem is to assign a set of resources/facilities to a set of locations in such a way as to minimize the total assignment cost. The assignment cost for a pair of facilities is a function of the flow between the facilities and the distance between the locations of the facilities.

## Algorithm Explanation

Data elements used:
* An n x n array (in the dataset file) that represents the "Manhattan distance" (Essentially 2-dimensional distance with a grid) between any two facilities. There are n facilities.
* An n x n array that represents the "flow" between any two facilities. The flow can be viewed as the traffic in the path. 
These arrays are stored in the ".dat" files in a format recognized by ```load\_data\_set.py```. Numpy is used for storing 2D arrays during execution.

An initial population is generated, shuffled,  and fitness scores are assigned to each member. The fitness scores are then normalised. 

Fitness of an element is calculated by its ```flow * distance``` product. Flows and distances are read from the flow[] and distance[] arrays. ```distance[x, y]``` is the Manhattan distance at matrix indices x, y. The same goes for flow.

Iterations are then run to select members or "chromosomes" with best fitnesses that are mutated or crossed. The population is then updated to the transformed one and the process is repeated for multiple iterations. 

All settings are configurable in ```configurations.py```. 


### Requirements:
* Python 3.6 or above (with pip)
    * numpy 1.18.2
    * plotly 4.5.4


### Usage Instructions:
1. Clone this repo
2. Navigate to the repo directory from the terminal/Command Prompt
3. Enter command `pip install -r requirements.txt` to install the required libraries
4. Enter `python3 main.py` or `py -3 main.py `


### Customizing options:

1. Navigate to ` configurations.py ` file , there you can change :

* DATA_SET : Filenames in /data folder
* CROSSOVER_PERCENTAGE 
* POPULATION_SIZE
* NUMBER_OF_GENERATIONS
* MUTATION_PERCENTAGE
* SLEEP_TIME
* GRAPH_AUTO_OPEN : IF True then plotly will open grpah in browser , else will save in /Graphs
* TURTLE_DRAW_ONE_BY_ONE : IF True the tutle component will draw lines one by one (se to true to see how the tutle is working)


### Details about the Data Set File :

The files contains :

        1. First Line = size of array , i.e = 12 -> two 12x12 arrays
        2. The First Matrix/Array represents the Manhattan Distances Between n = 12 Locations.

        EXAMPLE :

                MANHATTAN DISTANCES 

         LOCATION(X) | LOCATION(Y) | DISTANCE(X,Y)

                1         2               52
                3         7               25    


        3. The Second Matrix/Array represents the FLOW or ASSIGNMENT COST of n = 12 Resources/Facilities.


         EXAMPLE :

                FLOW/ASSIGMENT_COSTS 

         RESOURCE(X) | RESOURCE(Y) | FLOW(X,Y)

                1         4               2
                3         4               4 

## Approach 

The solution requires a permutation to be calculated ,  and then an OPTIMAL value be calculated .

eg : let p = {1,3,4,8} be a permutation matrix

then the optimal solution can be calculated by : 

f(1,3) + f(4,1) + f(1,8) + f(1,4) + ........ = 576 , where f(x,y) is the flow function of the resources permutation between Location x and y .


This approach uses the Evolutionary Algorithm techniques to come to the optimal Solution , through the following steps :

1. Generate a random population ( an array of arrays).
2. select the fittest chromosomes(an array from the population) by applying fitness and selection techniques.
3. Apply the CrossOver(Implemented) and Mutation(Not Yet Implemented) techniques to randomise the selected chromosome .
4. Calculate the Mean Fitness and Max Score of the best chromosome in the current generation.
5. Repeat the process for n number of generations while arrivig to the OPTIMAL solution.

### UML Diagram
![UML Diagram](/images/uml.png)
