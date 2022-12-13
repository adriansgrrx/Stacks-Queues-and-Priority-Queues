from graph import City

nodes, graph = City.load_graph("realpython_mat/roadmap.dot", City.from_dict)

# print(nodes["london"])
# print(graph)

# for neighbor in graph.neighbors(nodes["london"]): # built-in function .neighbors() syntax: Graph.neighbors(node)
#     print(neighbor.name)

# for neighbor, weights in graph[nodes["london"]].items():
#     print(weights["distance"], neighbor.name) # display weight edges

def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")
