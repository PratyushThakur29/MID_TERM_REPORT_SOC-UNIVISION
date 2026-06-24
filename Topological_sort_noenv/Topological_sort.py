import networkx as nx

# 1. Create a Directed Graph
G = nx.DiGraph()

# 2. Add the user's block connections (Edges)
G.add_edges_from([
    ("Load_Audio", "Filter_Noise"),
    ("Filter_Noise", "Plot_Graph",),
    ("Filter_Noise", "Works",),
    ("Plot_Graph","Nerd_Detect"),
    ("Nerd_Detect", "Works")
])

print(G)

# 3. Validate Acyclicity (No Loops)
if not nx.is_directed_acyclic_graph(G):
    print("Error: Loop detected! Cannot execute.")
else:
    # 4. Get the linear running execution order
    execution_order = list(nx.topological_sort(G))
    print("Valid graph! Execution order:", execution_order)