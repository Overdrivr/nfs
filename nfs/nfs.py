"""Near Field Scanner processing

Usage:
  nfs.py analyse --files=<pattern>
  nfs.py write2imgs  --start=<t1> --stop=<t2>
  nfs.py (-h | --help)
  nfs.py (-v | --version)

Options:
  -h --help         Show this screen.
  --version         Show version.
  --files=<pattern> Files to apply algorithm to. Simple filenames or patterns are supported.
  --start=<t1>      Start time for converting data files to 2D scan images.
  --stop=<t2>       Stop time for converting data files to 2D scan images.
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')

    if arguments['analyse']:
        pass
    elif arguments['write2imgs']:
        pass

    print(arguments)
