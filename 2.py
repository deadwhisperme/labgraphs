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

def call_friend(G, start, called):
    called.add(start)
    for neighbour in G[start]:
        if neighbour not in called:
            Tree.add_edge(start,neighbour)
            call_friend(G, neighbour, called)
G=graph()
Tree=nx.Graph()
called=set()
begin = input('Начальная точка ')
call_friend(G, begin, called)
nx.draw_spectral(Tree)
plt.show()


