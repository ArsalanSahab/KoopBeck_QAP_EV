import os
import numpy as np

from configurations import DATA_SET

# Read two-dimensional arrays from input file
def array_read_from_file(data_set_file) -> np.ndarray:

    array = []
    row_counter = 0

    while row_counter < array_size:

        line = data_set_file.readline()

        # Check if the read line is a string
        assert isinstance(line, str)

        # Append to array if not empty line
        if not line.isspace():
            row_counter += 1

            # Input line and split into a row array
            array_row = [int(element) for element in line.split(sep=' ') if element != '']
            array.append(array_row)

    # Convert to numpy array
    return np.array(array)

# Use the data file DATA_SET and reads line by line using the above method
with open(os.path.join('', 'data', DATA_SET), mode='r') as file:

    # read array size from data set file
    array_size = int(file.readline())

    # read distance array from data set file
    distance_array = array_read_from_file(file)

    # read flow array from data set file
    flow_array = array_read_from_file(file)
