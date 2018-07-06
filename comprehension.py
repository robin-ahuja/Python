import os
import glob
from pprint import pprint as pp

def main():
    file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
    pp(file_sizes)

if __name__ == '__main__':
    main()
