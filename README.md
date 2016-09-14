# Near-Field Scanner processing

Parse and processes efficiently large files produced by a near-field scanner.

# Installation
Try to make it compliant python 2.7 to cxfreeze it

Installation requires numpy and opencv modules
# Run

First, search the min/max amplitude, min/max coordinates & (x,y) step from all files matching a pattern.

```
python -m nfs.nfs analyse --files="*.dat"
```

This will generate a `nfs-search.json` file, required for the next step.

Then, generate all the images from the near-field scan, between a start time
and a stop time.

```
python -m nfs.nfs write2imgs -start="1e-9" -stop="5e-9"
```

Full command line usage
```
python -m nfs.nfs
```
# Test

```
pytest
```
