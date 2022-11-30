import sys
import numpy as np

matrix = None

if __name__ == '__main__':
    n = len(sys.argv)
    if n != 2:
        print("Please insert the path of the adjacency matrix as an argument")
        sys.exit("Program end")
    print("Adjacency matrix path: " + sys.argv[1])
    arr = np.loadtxt(sys.argv[1], delimiter=",", dtype=int)
    print(arr)
