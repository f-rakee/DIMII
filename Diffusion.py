import networkx as nx
import numpy as np
import math


def One_Round_Diffuse(g: nx.Graph, Seed_Set):
    Activated_Nodes = []
    new_activated = Seed_Set

    # Diffuse until its available
    while len(new_activated) != 0:
        new_activated = ICM_Diffuse(g, new_activated)
        Activated_Nodes = [*Activated_Nodes, *new_activated]

    Total_Length_Diffusion = len(Activated_Nodes)

    return Total_Length_Diffusion, Activated_Nodes


def ICM_Diffuse(g: nx.Graph, activated):
    current_activated = []

    # While there is a node in activated list chech diffusion
    while activated:
        if activated:
            node = activated.pop(0)
            for edge in g.out_edges(node, data=True):
                if edge[1] in set(g.graph['free']):

                    r = np.random.random()
                    New_Weight = edge[2]['new_weight']
                    if r < New_Weight:

                        # Node is activated
                        edge[2]['alpha'] = edge[2]['alpha'] + 1
                        current_activated.append(edge[1])
                        g.graph['free'].remove(edge[1])

                    else:
                        edge[2]['beta'] = edge[2]['beta'] + 1
            if node in g.graph['free']:
                g.graph['free'].remove(node)

    return current_activated
