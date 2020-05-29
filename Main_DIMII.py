import numpy as np
import networkx as nx
import Diffusion_seedTIMM_diffDomination_Thesis2
import NonDominated_Set_Algorithm_Thesis2
import Local_Update_seedTIMM_diffDomination_Thesis2
import TIMMBasedOnDomination_Thesis2
import NonDominatedSet_Modified2_9


Edges_List = "Edges list"
Trust_File = "Trust values"

(Num_Of_Edges, col) = Edges_List.shape
Unique_Nodes = np.unique(Edges_List)
Number_Of_Unique_Nodes = len(Unique_Nodes)


Budget = 50
K = 25
N = int(Budget / K)
Coefficient = 0

Counter_K_Fold = 1
Matrix_K_Fold_Spread = Counter_K_Fold * [0]
activated_each_iteration = N * [0]

for Counter in range(0, Counter_K_Fold):
    Alpha_Global = 1
    Beta_Global = 19

    All_Value_theta = [-1, 0, 1]
    p = [0.333, 0.333, 0.333]
    W = [1.0, 1.0, 1.0]
    q = len(All_Value_theta)

    Seed_Set = []
    Activated_Node = []

    # create the graph
    G = nx.DiGraph()
    G.add_edges_from(Edges_List)
    Edges = G.edges()
    G.graph['free'] = G.nodes()
    free_nodes = set(G.graph['free'])
    Nodes = G.nodes()

    # Adding Attribute to the edges
    Count_Initialize_Trust = 0
    for u, v, data in G.edges_iter(data=True):

        G.edge[u][v]['weight'] = 1 / G.in_degree(v)
        G.edge[u][v]['new_weight'] = 0
        G.edge[u][v]['Trust'] = Trust_File[Count_Initialize_Trust]
        G.edge[u][v]['alpha'] = Alpha_Global
        G.edge[u][v]['beta'] = Beta_Global
        Count_Initialize_Trust += 1

    for Count_Trial in range(0, N):
        print("The number of Trial: " + str(Count_Trial))

        Theta_TIM = TIM_Domination.calculate_theta(G, K)

        Calculate_Domination_Value.Find_NonDominated_Set(G)
        Calculate_Domination_Value.normalization(G)
        TIM_Domination.node_selection(G, K, Theta_TIM)

        Diffusion_seedTIMM_diffDomination_Thesis2.One_Round_Diffuse(G, list(Seed_Set_New))

        theta = 1
        Local_Update.Confidence_Bound(G, theta)
