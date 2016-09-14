from utilities.utilities import *
import glob
import json
import time

def writeimages(start, stop):
    f = open('config.json')
    config = json.load(f)
    xmin = config['xmin']
    xmax = config['xmax']
    ymin = config['ymin']
    ymax = config['ymax']
    minima = config['minima']
    maxima = config['maxima']
    filenames = config['filenames']
    timestep = config['timestep']
    step = config['step']

    startIndex = int(start / timestep)
    stopIndex  = int(stop  / timestep)
    timepointsAmount = stopIndex - startIndex

    print("Exporting data from %d to %d " % (startIndex, stopIndex))

    invstep =  round(1 / step, 2)

    print("1/step = %f" % invstep )

    dimx = int(round((xmax - xmin),3) * invstep) + 1
    dimy = int(round((ymax - ymin),3) * invstep) + 1

    print("Will create %d images of size (%d %d)" % (timepointsAmount, dimx, dimy))
    print("Type Enter to continue, Ctrl + C to abort")
    input()
    # Generate empty arrays for storing images
    images = []
    for i in range(timepointsAmount):
        images.append(np.zeros([dimx, dimy, 3]))

    print("Allocated image buffers. Main processing starting.")
    began = time.time()
    pixelcount = mainprocess(filenames, images, './imgscolor7/', startIndex=startIndex, stopIndex=stopIndex, minima=minima, maxima=maxima, timestep=timestep, xmin=xmin, ymin=ymin, invstep=invstep)
    ended = time.time()
    print("Processing took %f (s)" % (ended - began))
    print("Wrote %d / %d pixels" % (pixelcount, dimx * dimy * timepointsAmount))
