#! /usr/bin/env python3

import sys
from parse_temps import (parse_raw_temps)
from interpolation import (interpolation)
from leastSquares import (leastSquares)

def main():
    """
    This main function serves as the driver for the demo. Such functions
    are not required in Python. However, we want to prevent unnecessary module
    level (i.e., global) variables.
    """

    input_temps = sys.argv[1]
    fileToList = []
    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file):
            data = temps_as_floats
            fileToList.append(data)
        interpolation(fileToList)
        leastSquares(fileToList)



if __name__ == "__main__":

    main()
