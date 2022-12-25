import sys
import numpy as np
import os
import heapq

matrix = None
algo = 0
def Djisktra(arr):
    nb_nodes = len(arr)
    result_matrix = np.zeros(len(arr), dtype=object)  # initialisation de la matrice D à zero partout
    for i in range(nb_nodes):
        shortest_dist = sten(i, arr)
        #print(type(shortest_dist))
        result_matrix[i] = np.matrix(shortest_dist)
    print(type(result_matrix))
    print(type(result_matrix[0]))
    return result_matrix

def sten(source, adjacence_matrix):
    stnd = np.zeros(len(adjacence_matrix), dtype="int")
    stnd.fill(10**12)
    visited_nodes = np.zeros(len(adjacence_matrix), dtype="int")
    stnd[source]  = 0
    iter = 0
    while iter < len(arr):
        next_node = 0
        heap = []
        for i in range(len(arr)):
            if visited_nodes[i] == 0:
                heapq.heappush(heap,(stnd[i], i))
        next_node = heapq.heappop(heap)[1]
        visited_nodes[next_node] = 1
        for i in range(len(adjacence_matrix)):
            if not visited_nodes[i] and stnd[i] != 0 and stnd[i] > stnd[next_node] + adjacence_matrix[next_node][i]:
                stnd[i] = stnd[next_node] + adjacence_matrix[next_node][i]
        iter+=1
    return stnd

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
    print(type(distance[0]))
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
