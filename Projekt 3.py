from enum import Enum
from typing import Any, Callable
from typing import Optional
from typing import Dict, List
import networkx as nx
import matplotlib.pyplot as plt

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    def __init__(self, data):
        self.data = data

    data: Any
    index: int

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self, adjacencies):
        self.adjacencies = adjacencies

    def create_vertex(self, data: Any) -> Vertex:
        cortex = Vertex(data)
        self.adjacencies.update({cortex: []})
        return cortex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        sc = Edge()
        sc.source = source
        sc.destination = destination
        sc_graf = self.adjacencies.get(source)
        sc_graf.append(sc)

    def add_undirected_edge(self, edge: EdgeType, source: Vertex, destination: Vertex,
                            weight: Optional[float] = None) -> None:
        self.add_directed_edge(source, destination)
        self.add_directed_edge(destination, source)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == 1:
            self.add_directed_edge(source, destination)

        if edge == 2:
            self.add_undirected_edge(source, destination)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        pass

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        pass

    def show(self):
        G = nx.DiGraph()
        for x in self.adjacencies.values():
            for y in x:
               G.add_edge(y.source.data, y.destination.data)
        nx.draw(G, with_labels=True)
        plt.show()

    def print(self):
        for x in self.adjacencies.values():
            for y in x:
                print(y.source.data, "----->", y.destination.data)

def dead_path(g: Graph, cross_id: Any) -> Optional[List[Vertex]]:
    lista = []
    start = cross_id
    check = 0

    def fondue(a, lista, check):
        if check != 0:
            if a == start:
                return print(lista)
        check += 1

        for x in g.adjacencies.values():
            if x != []:
                for y in x:
                    if a == y.source.data:
                        lista.append(a)
                        fondue(y.destination.data, lista, check)
            else:
                return None

    return fondue(cross_id, lista, check)

slownik = {}
slownik2 = {}
slownik3 = {}
Graf1 = Graph(slownik)
Graf2 = Graph(slownik2)
Graf3 = Graph(slownik3)

vrt1 = Graf1.create_vertex(1)
vrt9 = Graf1.create_vertex(9)
vrt4 = Graf1.create_vertex(4)
vrt6 = Graf1.create_vertex(6)
Graf1.add_directed_edge(vrt1, vrt9)
Graf1.add_directed_edge(vrt9, vrt4)
Graf1.add_directed_edge(vrt4, vrt6)
Graf1.add_directed_edge(vrt6, vrt1)

vrtt45 = Graf2.create_vertex(45)
vrtt99 = Graf2.create_vertex(99)
vrtt3 = Graf2.create_vertex(3)
vrtt0 = Graf2.create_vertex(0)
Graf2.add_directed_edge(vrtt45, vrtt99)
Graf2.add_directed_edge(vrtt99, vrtt3)
Graf2.add_directed_edge(vrtt3, vrtt0)

vrttt1 = Graf3.create_vertex(1)
vrttt2 = Graf3.create_vertex(2)
vrttt3 = Graf3.create_vertex(3)
vrttt4 = Graf3.create_vertex(4)
vrttt5 = Graf3.create_vertex(5)
Graf3.add_directed_edge(vrttt1, vrttt2)
Graf3.add_directed_edge(vrttt2, vrttt5)
Graf3.add_directed_edge(vrttt2, vrttt3)
Graf3.add_directed_edge(vrttt3, vrttt4)
Graf3.add_directed_edge(vrttt4, vrttt1)

print("---------Graf 1-----------")
Graf1.show()
Graf1.print()
print("---------Graf 2-----------")
Graf2.show()
Graf2.print()
print("---------Graf 3-----------")
Graf3.show()
Graf3.print()
print("-------Tablica 1----------")
dead_path(Graf1, 9)
print("-------Tablica 2----------")
dead_path(Graf2, 45)
print("-------Tablica 3----------")
dead_path(Graf3, 1)