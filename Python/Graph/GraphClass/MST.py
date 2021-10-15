from Vertex import Vertex
from Graph import Graph


class MST:
    graph: Graph

    def __init__(self):
        self.graph = Graph()

    def create_graph(self, edges: list[list]) -> None:
        nodes = {}
        edge_list = {}
        num_of_nodes = 0
        graph = Graph()
        for i in edges:
            if i[0] not in nodes:
                nodes[i[0]] = num_of_nodes
                graph.add_vertex(i[0])
                num_of_nodes += 1
            if i[1] not in nodes:
                nodes[i[1]] = num_of_nodes
                graph.add_vertex(i[1])
                num_of_nodes += 1
            if nodes[i[0]] not in edge_list:
                edge_list[nodes[i[0]]] = []
            if nodes[i[1]] not in edge_list:
                edge_list[nodes[i[1]]] = []
            edge_list[nodes[i[0]]].append(nodes[i[1]])
            edge_list[nodes[i[1]]].append(nodes[i[0]])

        graph.init_adjacency_list()
        for e in edge_list:
            for v in edge_list[e]:
                graph.add_edge(e, v)

        # graph.display_nodes()
        # graph.display_edges()
        self.graph = graph

    def mst(self):
        self.graph.vertices[0].set_visited()
        stack = [0]
        while len(stack) > 0:
            current_node = stack[-1]
            temp = self.graph.get_adjacency_node(current_node)
            # print("Nodes: ", current_node, temp)
            if temp is None:
                stack.pop()
            else:
                self.graph.vertices[temp].set_visited()
                print(current_node, temp)
                stack.append(temp)


def main():
    edges = [
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['C', 'B'],
        ['D', 'B'],
        ['E', 'B'],
        ['C', 'D'],
        ['C', 'E'],
        ['D', 'E']
    ]

    graph = MST()
    graph.create_graph(edges)
    graph.mst()


if __name__ == '__main__':
    main()
