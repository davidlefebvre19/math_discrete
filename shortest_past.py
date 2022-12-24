import sys
import numpy as np
import os

matrix = None
algo = 0
INFINITY = float("inf")

def Djisktra(graph):
    global nb_nodes
    nb_nodes = len(graph)

    shortest_dists = np.zeros(shape = (nb_nodes, nb_nodes))
    for i in range(len(graph)):
        shortest_dists[i] = compute_dijkstra_from_src(graph, i)

    return shortest_dists

def compute_dijkstra_from_src(graph, src):
    """
    Computes the dijkstra algorithm on a graph, it computes all the shortest path from
    a source to all the other nodes of the graph and returns an array with the minimal distances.
    :param graph: 2D array : Matrix of costs representing the graph.
    :param src: Index of the node from which we want to compute all the shortest distances
    to the other nodes.
    :return: 1D array containing the computed shortest distances from the source to all the other nodes
    """
    dists = [INFINITY] * nb_nodes
    dists[src] = 0
    marked = [False] * nb_nodes

    n = 0
    while n < nb_nodes:
        x = get_min_dist_index(dists, marked)
        marked[x] = True

        for y in range(nb_nodes):
            if graph[x][y] > 0 and not marked[y] and dists[y] > dists[x] + graph[x][y]:
                dists[y] = dists[x] + graph[x][y]

        n += 1

    return dists

def get_min_dist_index(dists, marked):
    """
    This method works like a poll in an index priority queue, it returns the index of
    the node with the minimal distance.
    :param dists: Array of values representing the current distance of a node from the source.
    :param marked: Array of booleans representing the nodes that are already visited.
    :return: The index of the node with the minimal distance, the closest node.
    """
    val_min = INFINITY
    index_min = 0

    for v in range(nb_nodes):
        if dists[v] < val_min and not marked[v]:
            val_min = dists[v]
            index_min = v

    return index_min


def Bellman_Ford(arr):
    distance = np.zeros((len(arr), len(arr)))  # initialisation de la matrice D à zero partout
    for ligne in range(len(arr)):
        for colonne in range(len(arr)):
            if ligne != colonne:  # lorsque le nœud source et le nœud d'arrivé ne sont pas les mêmes (a vers a, b vers b, etc.)
                distance[ligne, colonne] = 10**12  # mettre la distance entre les deux nœuds = inf

    for source in range(len(arr)):  # permettra d'itérer sur la même ligne plusieurs fois pour pouvoir comparer un même nœud avec tout les autres
        for _ in range(len(arr) - 1):  # permettra de comparer tous les chemins possibles dans les autres lignes de la matrice d'adjacence
            for node in range(len(arr)):  # on boucle sur toutes les lignes (nœuds) de la matrice d'adjacence
                for neighbour in range(len(arr)):
                    # si la distance entre le nœud et le voisin est plus faible que celle actuelle, la remplacer
                    distance[source, neighbour] = min(distance[source, neighbour], distance[source, node] + arr[node, neighbour])

    return distance.astype(int)


def Floyd_Warshall(arr):
    matrix = np.asmatrix(arr)
    g = np.array(matrix)
    nodes = len(arr)
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    m_g = np.asmatrix(g)
    return m_g


if __name__ == '__main__':
    n = len(sys.argv)
    if n < 2:
        print("Please insert the path of the adjacency matrix as an argument")
        sys.exit("Program end")
    print("Adjacency matrix path: " + sys.argv[1])
    arr = np.genfromtxt(sys.argv[1], delimiter=",", dtype=float)
    print(arr)
    print("By default, the shortest path of every pair will be calculated using Djisktra, Bellman-Ford and "
          "Floyd_Warshall")
    try:
        if n == 3:
            Djisktra(arr)
        else:
            print(Djisktra(arr))
            print(Bellman_Ford(arr))
            print(Floyd_Warshall(arr))
        print("Shortest path computation done !")
    except:
        print("Shortest path computation error !")
