from typing import NamedTuple
import networkx as nx

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
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        ) # returns a new instance of the City class

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
