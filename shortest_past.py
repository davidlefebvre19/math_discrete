import sys
import numpy as np
import os
import heapq

matrix = None
algo = 0

# in : matrice d'adjacence d'un graphe
# out : matrice d'adjacence contenant les distances des plus court chemin entre un noeud et les autres noeuds du graphe
def Djisktra(arr):
    nb_nodes = len(arr)
    result_matrix = np.zeros((len(arr),len(arr)), dtype=object) # Matrice des distances des plus-court chemin
    for i in range(nb_nodes):
        shortest_dist = sten(i, arr) # Pour chaque noeud, cette fonction va nous donner un vecteur contenant les distances avec chaque noeud
        #print(shortest_dist)
        result_matrix[i] = np.matrix(shortest_dist)
    return result_matrix

def sten(source, adjacence_matrix):
    stnd = np.zeros(len(adjacence_matrix), dtype="int") # Vecteur contenant les distances avec les autres noeuds (STND: source to node distance)
    stnd.fill(10**12) # Les valeurs des distances sont initialisées à la valur symbolique "Infinity" (concept clef: aucune valeur n'est supérieure à celle-ci) mais à 10**12 dans notre algorithme (directive des consignes)
    visited_nodes = np.zeros(len(adjacence_matrix), dtype="int") # Vecteur contenant les noeuds qui ont été visités (0 : non-visité, 1 : visité)
    stnd[source] = 0 # Distance entre la source et la source = 0
    iter = 0
    while iter < len(adjacence_matrix): # On itère n fois, n = nombre de noeuds
        next_node = 0
        # Calcul du noeud le plus proche du noeud courant (-> prochain noeud que l'algorithme visitera)
        heap = [] # Utilisation d'un priority queue (inspiration provenant du livre "Algorithms, fourth edition") qui contiendra la liste des distances des noeuds qui sont accessible par le noeud source ET qui n'ont pas encore été visités
        for i in range(len(adjacence_matrix)):
            if visited_nodes[i] == 0: # Si le noeud n'a pas encore été visité...
                heapq.heappush(heap,(stnd[i], i)) # ... il est rajouté dans la heap
        next_node = heapq.heappop(heap)[1] # Nous prenons l'index du noeud correspondant à celui le plus proche de la source
        visited_nodes[next_node] = 1 # Ce noeud sera "visité" donc la valeur associée au noeud de la liste visited_nodes est actualisée à 1
        # Calcul du vecteur des distances
        for i in range(len(adjacence_matrix)):
            if not visited_nodes[i] and stnd[i] != 0 and stnd[i] > stnd[next_node] + adjacence_matrix[next_node][i]: # Ici nous avons pour objectif d'actualiser le vecteur des distances, cela se fait sous 3 conditions
                # ```not visited_nodes[i]``` : Le noeud en question ne doit pas être visité car cela voudrait dire qu'on rajouterai du chemin à un noeud qui  à déjà été visité (la valeur des distances ne serait plus la valeur des distances les plus courte)
                # ```stnd[i] != 0            : Lorsque stnd[i] = 0, cela correspond à la valeur de distance entre le noeud source et le noeud source, on ne calcule pas de valeur du plus court chemin dans ce cas-ci
                # ```stnd[i] > stnd[next_node] + adjacence_matrix[next_node][i]```: Si jamais le noeud est à visiter nous venons rajouter le coût du parcour de ce noeud avec le coût du chemin pour arriver au noeud précédent
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
    a = Djisktra(arr)
    print(Djisktra(arr))
    print("Bellman_Ford algorithm array :")
    b = Bellman_Ford(arr)
    print(Bellman_Ford(arr))
    print("Floyd_Warshall algorithm array :")
    c = Floyd_Warshall(matrix_g)
    print(Floyd_Warshall(matrix_g))

    if np.array_equal(a, b) and np.array_equal(a, c):
        print("All algorithms calculated the same shortest paths")
