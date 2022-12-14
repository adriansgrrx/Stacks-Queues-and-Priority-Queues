# Depth-First Search Using a LIFO Queue
import networkx as nx
from graph import (
    City,
    load_graph,
    depth_first_traverse,
    depth_first_search as dfs,
)
    
def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("realpython_mat/roadmap.dot", City.from_dict)
# Syntax: dfs_tree(G, source=None, depth_limit=None) --> Returns oriented tree constructed from a depth-first-search from source.
for node in nx.dfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")

print("\n****************************************************************************\n")

def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

nodes, graph = load_graph("realpython_mat/roadmap.dot", City.from_dict)
city = dfs(graph, nodes["edinburgh"], is_twentieth_century)
city.name

for city in depth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)