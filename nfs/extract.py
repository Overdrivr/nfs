import numpy as np
import glob
from utilities.utilities import *

# All files to process
filenames = glob.glob('*.dat')

# Get an iterator on all lines from all files
lines = linedispatch(filenames)

# min/max extraction and line parsing
for line in lines:
    # Extract data from raw line (=string)
    x, y, z, v, t = parseline(line)
    np.savetxt('test.csv', np.stack((t,v), axis=-1), delimiter=',')
    break
