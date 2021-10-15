from Vertex import Vertex


class Graph:
    vertices: list[Vertex]
    adj_matrix: list[list]
    number_of_nodes: int
    stack: list

    def __init__(self):
        self.vertices = []
        self.adj_matrix = []
        self.number_of_nodes = 0
        self.stack = []

    def add_vertex(self, v: str or int):
        node = Vertex(v)
        self.number_of_nodes += 1
        self.vertices.append(node)
        self.adj_matrix.append([])

    def init_adjacency_list(self):
        self.adj_matrix = [[0 for i in range(self.number_of_nodes)] for i in range(self.number_of_nodes)]

    def add_edge(self, from_node: int, to_node: int) -> None:
        self.adj_matrix[from_node][to_node] = 1
        # self.adj_matrix[to_node].append(from_node)

    def display_nodes(self):
        for i in self.vertices:
            print(i.name, end=" ")
        print()

    def display_edges(self):
        for i in self.adj_matrix:
            print(i)

    def get_adjacency_node(self, v: int) -> int or None:
        for i in range(self.number_of_nodes):
            if self.adj_matrix[i][v] == 1 and not self.vertices[i].visited:
                return i
        return None
