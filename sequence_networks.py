import matplotlib.pyplot as plt
import networkx as nx

def draw_sequence_network():
    G = nx.DiGraph()
    G.add_nodes_from(["Z1","Z2","Z0"])
    G.add_edges_from([("Z1","Z2"),("Z2","Z0")])

    fig = plt.figure(figsize=(5,4))
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=3000)
    plt.title("Sequence Network Diagram")
    return fig
