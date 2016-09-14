from utilities.utilities import *
import glob
import json
import time

# TODO: Add checks that timepoints are always constant between lines
# TODO: Add checks that timestep is constant for a given line

def analyse(filenames):
    minima = None
    maxima = None
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    step = 0.1
    maxvtime = None

    xcoords = []
    ycoords = []

    # To store timepoints
    timepoints = None

    began = time.time()

    # Get an iterator on all lines from all files
    lines = linedispatch(filenames)

    # min/max extraction and line parsing
    for line in lines:
        # Extract data from raw line (=string)
        x, y, z, v, t = parseline(line)

        xcoords.append(x)
        ycoords.append(y)

        print("Location : %f %f %f" % (x,y,z))

        # Init minima/maxima
        if minima is None:
            minima = v[0]

        if maxima is None:
            maxima = v[0]

        if xmin is None:
            xmin = x

        if ymin is None:
            ymin = y

        if xmax is None:
            xmax = x

        if ymax is None:
            ymax = y

        if timepoints is None:
            timepoints = np.array(t)

        # Compute min/max
        minima = min(minima, min(v))
        maxima = max(maxima, max(v))
        xmin = min(xmin, x)
        ymin = min(ymin, y)
        xmax = max(xmax, x)
        ymax = max(ymax, y)


    ended = time.time()
    print("Processing took %f (s)" % (ended - began))

    print("Min/Max : %f %f " % (minima, maxima))

    xcoords = xcoords.sort()
    ycoords = ycoords.sort()

    xsteps = [v1-v0 for v1, v0 in zip(xcoords[1::2], xcoords[0::2])]
    ysteps = [v1-v0 for v1, v0 in zip(ycoords[1::2], ycoords[0::2])]

    # Compute min xstep, min ystep, max xstep, max ystep
    xstepmin = min(xsteps)
    ystepmin = min(ysteps)
    xstepmax = max(xsteps)
    ystepmax = max(ysteps)

    print("MinMax step along x axis : (%f,%f)" % (xstepmin, xstepmax))
    print("MinMax step along y axis : (%f,%f)" % (ystepmin, ystepmax))

    # TODO: Handle what happen if step is not constant

    # For now, keep xmin as step

    results = dict(
    filenames=filenames,
    minima=minima,
    maxima=maxima,
    xmin=xmin,
    ymin=ymin,
    xmax=xmax,
    ymax=ymax,
    timestep=(timepoints[1] - timepoints[0]),
    step=xstepmin
    )

    f = open('config.json', 'w')
    json.dump(results, f)
    f.close()

    f = open('timepoints.json', 'w')
    for t in timepoints:
        f.write(str(t))
        f.write('\n')
    f.close()
