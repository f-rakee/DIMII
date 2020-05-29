import numpy as np
import networkx as nx
import math
import random
import operator


def Find_NonDominated_Set(g: nx.DiGraph):
    free_nodes = set(g.graph['free'])
    # Find size nondominated set for all nodes
    for i in g.nodes():
        nds_i = 0
        neighbors_current_node = g.neighbors(i)
        for cur_neighbor in neighbors_current_node:
            counter_d = 0
            In_Edges_Current_Child = g.in_edges(cur_neighbor, data=True)
            weight_current_neighbor = 0
            for j in In_Edges_Current_Child:
                if (g.edge[i][cur_neighbor]['weight'] == g.edge[j[0]][cur_neighbor]['weight'] and
                            g.edge[i][cur_neighbor]['Trust'] < g.edge[j[0]][cur_neighbor]['Trust']) or \
                        (g.edge[i][cur_neighbor]['weight'] < g.edge[j[0]][cur_neighbor]['weight'] and
                                 g.edge[i][cur_neighbor]['Trust'] == g.edge[j[0]][cur_neighbor]['Trust']) or \
                        (g.edge[i][cur_neighbor]['weight'] < g.edge[j[0]][cur_neighbor]['weight'] and
                                 g.edge[i][cur_neighbor]['Trust'] < g.edge[j[0]][cur_neighbor]['Trust']):
                    counter_d += 1
                else:
                    weight_current_neighbor += 1
            if counter_d == 0:
                nds_i += 1

            g.edge[i][cur_neighbor]['new_weight'] = weight_current_neighbor
        if i in free_nodes:
            g.node[i]['Length_NonDminated_Set'] = nds_i
        else:
            g.node[i]['Length_NonDminated_Set'] = -math.inf


def normalization(g: nx.Graph):
    for i in g.nodes():
        sum_new_weight = 0
        in_edges = g.in_edges(i, data=True)
        for j in in_edges:
            sum_new_weight += g.edge[j[0]][j[1]]['new_weight']
        for k in in_edges:
            g.edge[k[0]][k[1]]['new_weight'] = g.edge[k[0]][k[1]]['new_weight'] / sum_new_weight

