# networkx represents graph nodes using textual identifiers that can optionally 
# have an associated dictionary of attributes
import networkx as nx
print(nx.nx_agraph.read_dot("realpython_mat/roadmap.dot")) # read_dot() returns a networkx MultiGraph or \
                                                            # MultiDiGraph from the dot file with the path.

graph = nx.nx_agraph.read_dot("realpython_mat/roadmap.dot")
print(graph.nodes["london"])

# my 🔑 key take-away here is that, it is just like accessing an object or a dictionary present in the dot file.