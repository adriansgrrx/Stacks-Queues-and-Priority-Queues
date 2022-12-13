from graph import City

nodes, graph = City.load_graph("realpython_mat/roadmap.dot", City.from_dict)

# print(nodes["london"])
# print(graph)

# for neighbor in graph.neighbors(nodes["london"]): # built-in function .neighbors() syntax: Graph.neighbors(node)
#     print(neighbor.name)

for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name) # display weight edges
