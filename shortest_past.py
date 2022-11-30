import sys
import numpy as np
import os

matrix = None
algo = 0


def Djisktra(arr):
    return


def Bellman_Ford(arr):
    return


def Floyd_Warshall(arr):
    return


if __name__ == '__main__':
    n = len(sys.argv)
    if n < 2:
        print("Please insert the path of the adjacency matrix as an argument")
        sys.exit("Program end")
    print("Adjacency matrix path: " + sys.argv[1])
    arr = np.loadtxt(sys.argv[1], delimiter=",", dtype=int)
    # print(arr)
    print("By default, the shortest path of every pair will be calculated using Djisktra, Bellman-Ford and "
          "Floyd_Warshall")
    try:
        if n == 3:
            Djisktra(arr)
        else:
            Djisktra(arr)
            Bellman_Ford(arr)
            Floyd_Warshall(arr)
        print("Shortest path computation done !")
    except:
        print("Shortest path computation error !")
