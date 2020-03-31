# KoopBeck_QAP_EV
Koopmans-Beckmann Quadratic Assignment Problem Minimisation Through Evolutionary Algorithm



## Problem Definition

The quadratic assignment problem was introduced by Koopmans and Beckman in 1957 . The objectives of the problem is to assign a set of resources/facilities to a set of locations in such a way as to minimize the total assignment cost. The assignment cost for a pair of facilities is a function of the flow between the facilities and the distance between the locations of the facilities.


### Steps to download and run 

#### Note : Must have python version 3.6 or above installed (and added to path)


1. Click on the green button `Clone or Download` to download the repo.
2. Extract the contents.
3. Through commandprompt/termial navigate to the downloaded repo directory.
4. Type the command ` pip install -r requirements.txt ` to install the required libraries.
5. After the above , Type the command : ` python3 main.py `.


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