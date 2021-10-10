from GraphnIntroduction import AdjacencyListGraph


class DFS(AdjacencyListGraph):

    def traverse_graph(self):
        stack = []
        visited_nodes = [0 for i in range(self.number_of_nodes)]
        current_node = 0
        stack.append(current_node)
        while len(stack) != 0:
            if visited_nodes[current_node] == 0:
                visited_nodes[current_node] = 1
                stack.append(current_node)
                print(current_node, end=" ")
            all_child_visited = True
            for i in self.node_list[current_node]:
                if visited_nodes[i] == 0:
                    all_child_visited = False
                    current_node = i
                    break
            if all_child_visited:
                stack.pop()
        print()


def main():
    arr = [[1, 2], [2, 3], [2, 4], [3, 4]]
    n = 4
    list_graph = DFS(n)
    for edge in arr:
        list_graph.insert_nodes(edge[0] - 1, edge[1] - 1)
    list_graph.print_graph()
    list_graph.traverse_graph()


if __name__ == "__main__":
    main()
