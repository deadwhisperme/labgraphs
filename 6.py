import matplotlib.pyplot as plt
import networkx as nx
def graph():
    N = int(input('Кол-во вершин '))
    weight = [[float('+inf')]*N for j in range(N)]
    for i in range(N):
        weight[i][i] = 0
    M = int(input('Коло-во ребер'))
    for i in range(M):
        a, b, w = input().split()
        a, b, w = int(a), int(b), float(w)
        weight[a][b] = w
        weight[b][a] = w
    return weight

def printmatrix(A):
    for i in range(len(A)):
        print(*A[i], sep='\t')
    print()

from copy import deepcopy

def floyd(weight):
    N = len(weight)
    F = deepcopy(weight)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                F[i][j] = min(F[i][j], F[i][k] + F[k][j])
    return F


G = graph()
printmatrix(G)
F = floyd(G)
printmatrix(F)
