from graph import City

nodes, graph = City.load_graph("realpython_mat/roadmap.dot", City.from_dict)

print(nodes["london"])
print(graph)