# Shortest Path Using Breadth-First Traversal
import networkx as nx
from graph import City, load_graph

nodes, graph = load_graph("realpython_mat/roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1): # networkx built-in function all_shortest_paths 
    print(f"{i}.", " → ".join(city.name for city in path))               # to find the "shortcut" or the best path.