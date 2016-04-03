import matplotlib.pyplot as plt
import networkx as nx
def graph():
    inp3 = open("./inp3.txt","r")
    ls = inp3.readlines()
    G = {}
    for i in range(len(ls)):
        ls[i] = ls[i].rstrip()
        a, b, weight = ls[i].split()
        weight = float(weight)
        if a not in G:
            G[a] = {b:weight}
        else:
            G[a][b] = weight
        if b not in G:
            G[b] = {a:weight}
        else:
            G[b][a] = weight
    return G

def dejkstra(G, start):
    shortest_path = {vertex:float('+inf') for vertex in G}
    shortest_path[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in G[current]:
            offering_shortest_path = shortest_path[current] + G[current][neighbour]
            if offering_shortest_path < shortest_path[neighbour]:
                shortest_path[neighbour] = offering_shortest_path
                queue.append(neighbour)
    return shortest_path
def shortest(G, start, finish):
    d = dejkstra(G, start)
    r = finish
    p=[]
    while r:
        p.append(r)
        r = d[r][1]
    return p[::-1]
G = graph()
begin = input('Начальная точка ')
finish = input('Конечная точка ')
print(shortest(G,begin,finish))

