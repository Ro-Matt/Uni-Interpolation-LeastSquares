# Uni-Interpolation-LeastSquares

# Getting Started

**Language:** Python 3.9

# Requirements

**parseTemps.py**
import sys
from parse_temps import (parse_raw_temps)
from interpolation import (interpolation)
from leastSquares import (leastSquares)

**parse_temps.py**
import re
from typing import (TextIO, Iterator, List, Tuple)

**interpolation.py**
import os.path

**leastSquares.py**
import os.path
import numpy as np
from sympy import Matrix

# Compilation & Execution Instructions

./parseTemps.py EXAMPLE.txt 
