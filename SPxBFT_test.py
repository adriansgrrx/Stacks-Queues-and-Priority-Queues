# Shortest Path Using Breadth-First Traversal
import networkx as nx
from graph import City, load_graph
from graph import shortest_path
from graph import connected

nodes, graph = load_graph("realpython_mat/roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

print("\nUsing networkx:")
for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1): # networkx built-in function all_shortest_paths 
    print(f"{i}.", " → ".join(city.name for city in path))               # to find the "shortcut" or the best path.

print("*****************************************************************")

# queue-based implementation of the shortest path, we can get the same results as with networkx.
print("Queue-based implementation:")
print(" → ".join(city.name for city in shortest_path(graph, city1, city2)))

def by_latitude(city):
    return -city.latitude #To enforce a descending order, we add the minus sign (-) in front of the .latitude attribute.

print(" → ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)
))

print("***************************** CONNECTED or NOT ************************************")
print(connected(graph, nodes["belfast"], nodes["glasgow"]))
print(connected(graph, nodes["belfast"], nodes["derry"]))