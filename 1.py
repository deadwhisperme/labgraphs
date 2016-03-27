import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
N = int(input('Кол-во рёбер'))
for i in range(N):
    r = list(input().split())
    if len(r)==2:
        G.add_edge(r[0],r[1])
    elif len(r)==1:
        G.add_node(r[0])
nx.draw(G)
plt.savefig("simple_path.png")
plt.show()
