
# graph is representation of set of objects where objects are connected by links
# interconnected objects are termed as vertices
# links that connect the vertices are called edges


class Graph(object):
    def __init__(self, graph=None):             # initialize graph
        if graph is None:
            graph = {}
        self.graph = graph

    def vertices(self):
        return list(self.graph.keys())          # returns the list of vertices

    def edges(self):                            # returns the list of edges
        edges = []
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def add_vertex(self, vertex):               # function to add new vertex
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, edge):                   # function to add new edges
        edge = tuple(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

g = {1: [4], 2: [3], 3: [2, 3, 4, 'e'], 4: [1, 3], 'e': [3], 'f': []}

graph = Graph(g)

print('vertices of graph:')
print(graph.vertices())

print('edges of graph:')
print(graph.edges())

print('add vertex')
graph.add_vertex('g')

print('vertices of graph:')
print(graph.vertices())

print('add an edge:')
graph.add_edge({1, 'g'})

print('vertices of graph:')
print(graph.vertices())

print('edges of graph:')
print(graph.edges())

print('adding an edge with new vertices:')
graph.add_edge({'h', 'i'})
print('vertices of graph:')
print(graph.vertices())
print('edges of graph:')
print(graph.edges())
