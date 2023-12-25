from __future__ import annotations
from functools import reduce
from networkx import Graph, connected_components, minimum_edge_cut

def day25a(input: list[str]) -> int:
    graph = Graph()

    for line in input:
        node, connections = line.split(": ")
        graph.add_node(node)
        
        for connection in connections.split(" "):
            graph.add_node(connection)

            if node > connection: graph.add_edge(connection, node)
            else: graph.add_edge(node, connection)

    graph.remove_edges_from(minimum_edge_cut(graph))

    return reduce(lambda acc, component: acc * len(component), connected_components(graph), 1)
