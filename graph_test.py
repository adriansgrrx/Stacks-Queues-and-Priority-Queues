# import networkx as nx
from graph import (
    City,
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,
)
# nodes, graph = City.load_graph("realpython_mat/roadmap.dot", City.from_dict)

# print(nodes["london"])
# print(graph)

# for neighbor in graph.neighbors(nodes["london"]): # built-in function .neighbors() syntax: Graph.neighbors(node)
#     print(neighbor.name)

# for neighbor, weights in graph[nodes["london"]].items():
#     print(weights["distance"], neighbor.name) # display weight edges

# def sort_by(neighbors, strategy):
#     return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

# def by_distance(weights):
#     return float(weights["distance"])

# for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
#     print(f"{weights['distance']:>3} miles, {neighbor.name}")

# **********************************************
# Using built-in function, nx.bfs_tree() to know the certain year 
# the city got its status with a certain year condition
def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000
# ***************************************************************************
# def order(neighbors):
#     def by_latitude(city):
#         return city.latitude
#     return iter(sorted(neighbors, key=by_latitude, reverse=True))
# ***************************************************************************
nodes, graph = load_graph("realpython_mat/roadmap.dot", City.from_dict)
# ***************************************************************************
# for node in nx.bfs_tree(graph, nodes["edinburgh"]):
#     print("📍", node.name)
#     if is_twentieth_century(node.year):
#         print("Found:", node.name, node.year)
#         break
# else:
#     print("Not found")
# ***************************************************************************
# for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
#     print("📍", node.name)
#     if is_twentieth_century(node.year):
#         print("Found:", node.name, node.year)
#         break
# else:
#     print("Not found")
# ***************************************************************************
city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
city.name

for city in breadth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)