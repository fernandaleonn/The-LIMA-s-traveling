import matplotlib.pyplot as plt
import networkx as nx

def grafo_generator(route):

    color_map = ["red"]
    for i in range(1, len(route) - 1):
        color_map.append("aqua")
    rg = [route[i:i+2] for i in range(len(route) -  1)]
    g = nx.Graph()
    g.add_edges_from(rg)
    return nx.draw(g, with_labels=True, node_color=color_map )

