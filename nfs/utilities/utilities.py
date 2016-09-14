import numpy as np
from fastnumbers import fast_float
import os
import cv2
import math

def linedispatch(files):
    for filename in files:
        # Open file
        f = open(filename)
        # Read it, line by line
        for line in f:
            yield line

def parseline(line, startIndex=0, stopIndex=-1):
    # Slice the line using space as delimiter, and convert to float
    line = np.fromstring(line, sep=' ')

    # Extract x, y, z
    x, y, z = float(line[0]), float(line[1]), float(line[2])

    # Extract v(t) curve (t is at even indexes, v at odd indexes)
    t = np.array([float(i) for i in line[(3+startIndex*2):stopIndex*2:2]])
    v = np.array([float(i) for i in line[(4+startIndex*2):stopIndex*2:2]])

    return x, y, z, v, t

def minmaxline(line):
    # Slice the line using space as delimiter, and convert to float
    line = [fast_float(i) for i in line.split()]

    # Search min/max without building new objects
    minima = min(line[4::2])
    maxima = max(line[4::2])

    return minima, maxima

def minmaxsearch(v):
    return min(v), max(v)

def pointdispatch(t, v):
    for time,amplitude in zip(t,v):
        yield time, amplitude

def rgb(minimum, maximum, value):
    # Ensure float numbers are used
    minimum, maximum = float(minimum), float(maximum)
    # Compute ratio
    ratio = 2 * (value-minimum) / (maximum - minimum)
    # Compute red green blue from ratio for colorscale
    r = int(max(0, 255*(ratio - 1)))
    b = int(max(0, 255*(1 - ratio)))
    g = 255 - b - r

    return r, g, b

def extractPixels(t, v, minima=0.0, maxima=1.0):
    # Get an iterator over all the timepoints of the line
    points = pointdispatch(t, v)

    # Calculate pixel color
    for time, amplitude in points:
        r,g,b = rgb(minima, maxima, amplitude)
        yield time, r, g, b

def mainprocess(filenames, outputArrs, outputFolder, startIndex=0, stopIndex=0, minima=0.0, maxima=1.0, timestep=0.1, xmin=0.0, ymin=0.0, invstep=10):
    # Create output folder
    if not os.path.exists(outputFolder):
        os.mkdir(outputFolder)

    # Get an iterator on all lines from all files
    lines = linedispatch(filenames)

    pixelcount = 0
    linecount = 0

    invtimestep = round(1 / timestep, 3)
    print("1/timestep: %f" % invtimestep)

    # min/max extraction and line parsing
    for line in lines:
        # Extract data from raw line (=string)
        x, y, z, v, t = parseline(line, startIndex=startIndex, stopIndex=stopIndex)
        print("Location : %f %f %f" % (x,y,z))
        linecount += 1
        # Extract all pixels by parsing the line
        pixels = extractPixels(t,v, minima=minima, maxima=maxima)

        for time, r, g, b in pixels:
            index = int(time * invtimestep)

            if index < startIndex or index > stopIndex:
                continue

            # Identify to which image the point belongs using the time value for this point
            imgId = index - startIndex

            # Identify the pixel position inside this identified image
            ix = math.trunc(round((x - xmin),3) * invstep)
            iy = math.trunc(round((y - ymin),3) * invstep)

            pixelcount += 1

            # Write the pixel
            outputArrs[imgId][ix, iy, 0] = b
            outputArrs[imgId][ix, iy, 1] = g
            outputArrs[imgId][ix, iy, 2] = r

        # Write to image every 500 lines
        if linecount % 501 == 0:
            print("Write images")
            for i in range(len(outputArrs)):
                cv2.imwrite(os.path.join(outputFolder, 'img_' + str(i) + '.png'), outputArrs[i])

    # Write final images
    for i in range(len(outputArrs)):
        cv2.imwrite(os.path.join(outputFolder, 'img_' + str(i) + '.png'), outputArrs[i])

    return pixelcount
