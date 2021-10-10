from Vertex import Vertex


class Graph:
    vertices: list[Vertex]

    def add_vertex(self, v: Vertex):
        self.vertices.append(v)


    def add_edge(self, u: Vertex, v: Vertex):
        pass