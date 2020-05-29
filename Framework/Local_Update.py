import numpy as np
import networkx as nx

def Confidence_Bound(g: nx.Graph, theta):
    for u, v in g.edges_iter():
        mean = g.edge[u][v]['alpha'] / (g.edge[u][v]['alpha'] + g.edge[u][v]['beta'])

        variance = (1 / g.edge[u][v]['alpha'] + g.edge[u][v]['beta']) * np.math.sqrt(
            (g.edge[u][v]['alpha'] * g.edge[u][v]['beta']) / (g.edge[u][v]['alpha'] + g.edge[u][v]['beta'] + 1))

        g.edge[u][v]['weight'] = mean + theta * variance
    for node in g.nodes():

        sum_weight = 0
        for edge in g.in_edges(node, data=True):
            sum_weight += edge[2]['weight']
        for edge2 in g.in_edges(node, data=True):
            edge2[2]['weight'] = edge2[2]['weight'] / sum_weight