# KoopBeck_QAP_EV
Koopmans-Beckmann Quadratic Assignment Problem Minimisation Through Evolutionary Algorithm


<<<<<<< HEAD
=======

## Problem Definition

The quadratic assignment problem was introduced by Koopmans and Beckman in 1957 . The objectives of the problem is to assign a set of resources/facilities to a set of locations in such a way as to minimize the total assignment cost. The assignment cost for a pair of facilities is a function of the flow between the facilities and the distance between the locations of the facilities.


### Steps to download and run 
>>>>>>> b1aa74153189334fb6aeda61e3ddf1d4995ac7a6

### Requirements:
+Python 3.6 or above (with pip)
    +numpy 1.18.2
    +plotly 4.5.4


<<<<<<< HEAD
### Usage Instructions:
1. Clone this repo
2. Navigate to the repo directory from the terminal/Command Prompt
3. Enter command `pip install -r requirements.txt` to install the required libraries
4. Enter `python3 main.py`

### UML Diagram
![UML Diagram](/images/uml.png)
=======
1. Click on the green button `Clone or Download` to download the repo.
2. Extract the contents.
3. Through commandprompt/termial navigate to the downloaded repo directory.
4. Type the command ` pip install -r requirements.txt ` to install the required libraries.
5. After the above , Type the command : ` python3 main.py `.
                     Alternative :      ` py  -3 main.py `.


### To Customise Options please follow the steps :

1. Navigate to ` configurations.py ` file.
2. You can Change : 

        . DATA_SET : Filenames in /data folder
        . CROSSOVER_PERCENTAGE 
        . POPULATION_SIZE
        . NUMBER_OF_GENERATIONS


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
>>>>>>> b1aa74153189334fb6aeda61e3ddf1d4995ac7a6
