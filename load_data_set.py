import os
import numpy as np


#### CUSTOM IMPORTS ####
from configurations import DATA_SET

# FUNCTION TO READ THE 2D ARRAYS FROM DATA SET

def array_read_from_file(data_set_file) -> np.ndarray:

    array = []

    row_counter = 0

    while row_counter < array_size:

        line = data_set_file.readline()

        assert isinstance(line, str)

        if not line.isspace():

            row_counter += 1
            array_row = [int(element) for element in line.split(sep=' ') if element != '']
            array.append(array_row)

    return np.array(array)


with open(os.path.join('', 'data', DATA_SET), mode='r') as file:

    # read array size from data set file
    array_size = int(file.readline())

    # read distance array from data set file
    distance_array = array_read_from_file(file)

    # read flow array from data set file
    flow_array = array_read_from_file(file)
