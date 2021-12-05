from abc import ABC, abstractmethod


class Graph(ABC):
    number_of_nodes: int

    @abstractmethod
    def print_graph(self):
        pass

    def insert_nodes(self, node1: int, node2: int) -> bool or None:
        pass


class AdjacencyMatrixGraph(Graph):
    matrix: list[list[int]]

    def __init__(self, n: int):
        self.number_of_nodes = n
        self.matrix = [[0 for col in range(n)] for row in range(n)]

    def insert_nodes(self, node1: int, node2: int) -> bool or None:
        if node1 is None or node2 is None:
            return False
        if node1 > self.number_of_nodes or node2 > self.number_of_nodes:
            return False
        self.matrix[node1][node2] = 1
        self.matrix[node2][node1] = 1
        return True

    def print_graph(self):
        for row in self.matrix:
            for col in row:
                print(col, end=" ")
            print()


class AdjacencyListGraph(Graph):
    node_list: list[list[int]]

    def __init__(self, n: int):
        self.number_of_nodes = n
        self.node_list = [[] for i in range(n)]

    def insert_nodes(self, node1: int, node2: int) -> bool or None:
        if node1 is None or node2 is None:
            return False
        if node1 > self.number_of_nodes or node2 > self.number_of_nodes:
            return False
        self.node_list[node1].append(node2)
        self.node_list[node2].append(node1)
        return True

    def print_graph(self):
        for row in self.node_list:
            for col in row:
                print(col, end=" ")
            print()


def main():
    arr = [[1, 2], [2, 3], [2, 4], [3, 4]]
    n = 4
    matrix_graph = AdjacencyMatrixGraph(n)
    for edge in arr:
        matrix_graph.insert_nodes(edge[0] - 1, edge[1] - 1)
    matrix_graph.print_graph()

    print()

    list_graph = AdjacencyListGraph(n)
    for edge in arr:
        list_graph.insert_nodes(edge[0] - 1, edge[1] - 1)
    list_graph.print_graph()


if __name__ == "__main__":
    main()

