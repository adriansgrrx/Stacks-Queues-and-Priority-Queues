from typing import NamedTuple
import networkx as nx
from queues import Queue
from collections import deque

class City(NamedTuple): # NamedTuples contain keys that are hashed to a particular value. 
    name: str           # it supports both access from key-value and iteration.
    country: str
    year: int | None
    latitude: float
    longitude: float

    @classmethod # @classmethod decorator is used to declare a method in the class as a class
                    #⬇ cls implies that the method belongs to the class
    def from_dict(cls, attrs): # from_dict() class method takes a dictionary of attributes extracted from a DOT file
        return cls(
            name = attrs["xlabel"],
            country = attrs["country"],
            year = int(attrs["year"]) or None,
            latitude = float(attrs["latitude"]),
            longitude = float(attrs["longitude"]),
        ) # returns a new instance of the City class


# Breadth-First Search Using a FIFO Queue
def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data=True)
    }
    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights) # Each edge of a graph has an associated numerical value, called a weight.
        for name1, name2, weights in graph.edges(data=True)
    )

def breadth_first_traverse(graph, source, order_by=None):
    queue = Queue(source)
    visited = {source}
    while queue:
        yield (node := queue.dequeue())
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

def breadth_first_search(graph, source, predicate, order_by=None):
    for node in breadth_first_traverse(graph, source, order_by):
        if predicate(node):
            return node
            
# Shortest Path Using Breadth-First Traversal
def shortest_path(graph, source, destination, order_by=None):
    queue = Queue(source)
    visited = {source}
    previous = {}
    while queue:
        node = queue.dequeue()
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
                previous[neighbor] = node
                if neighbor == destination:
                    return retrace(previous, source, destination)
                    
# To recreate the shortest path between the source and destination
def retrace(previous, source, destination):
    path = deque()
    current = destination
    while current != source:
        path.appendleft(current)
        current = previous.get(current)
        if current is None:
            return None

    path.appendleft(source)
    return list(path)

# breadth-first traversal tells whether two nodes remain connected or not.
def connected(graph, source, destination):
    return shortest_path(graph, source, destination) is not None