import matplotlib.pyplot as plt
import networkx as nx
def graph():
    G = {}
    N = int(input('Кол-во рёбер'))
    for i in range(N):
        a, b = input().split()
        if a not in G:
            G[a] = {b}
        else:
            G[a].add(b)
        if b not in G:
            G[b] = {a}
        else:
            G[b].add(a)
    return G

def bfs_fired(G, start, fired):
    Q=[start]
    fired.add(start)
    while len(Q)!=0:
        current= Q.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                Tree.add_edge(current, neighbour)
                Q.append(neighbour)

G=graph()
Tree=nx.Graph()
fired=set()
begin = input('Начальная точка ')
bfs_fired(G, begin, fired)
nx.draw_spectral(Tree)
plt.show()

