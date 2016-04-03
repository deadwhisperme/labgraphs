import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
inp = open("./inp.txt","r")
ls = inp.readlines()
for i in range(len(ls)):
    ls[i] = ls[i].rstrip()
    r = list(ls[i].split())
    if len(r)==2:
        G.add_edge(r[0],r[1])
    else:
        G.add_node(r[0])
nx.draw(G)
plt.savefig("simple_path.png")
plt.show()
