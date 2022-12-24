import sys
import numpy as np
import os
import heapq

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


def Floyd_Warshall(c: np.matrix):
    g = np.array(c) # convertir la matrice c en un np.array
    nodes = len(c) # récupérer la taille d'une ligne pour pouvoir boucler
    for k in range(nodes): # permettra de comparer un chemin i -> j avec un chemin i -> j -> k
        for i in range(nodes):  # source
            for j in range(nodes): # destination
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]) # on garde le coût minimum entre le coût du chemin actuel (i,j) et celui passant par k en intermédiaire
    return g.astype(int) # return la matrice de distance g


if __name__ == '__main__':
    arr = np.loadtxt('data.csv', delimiter=",")
    matrix_g = np.asmatrix(arr) #convertir np.array en np.matrix pour respecter la signature
    print("By default, the shortest path of every pair will be calculated using Djisktra, Bellman-Ford and "
          "Floyd_Warshall")

    print("Djiskstra algorithm array :")
    print(Djisktra(arr))
    print("Bellman_Ford algorithm array :")
    print(Bellman_Ford(arr))
    print("Floyd_Warshall algorithm array :")
    print(Floyd_Warshall(matrix_g))
