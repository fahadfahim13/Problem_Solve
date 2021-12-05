def dfs_from_node(edges: list[list[int]], node: int, total_nodes: int) -> bool:
    if edges is None or len(edges) == 0 or total_nodes <= 0 or not 0 <= node < total_nodes:
        return False
    total_visited = 0
    visited = [False for i in range(total_nodes)]
    stack = [node]
    while len(stack) > 0:
        temp = stack[-1]
        if not visited[temp]:
            visited[temp] = True
            total_visited += 1
        new_node_found = False
        for i in edges[temp]:
            if not visited[i]:
                new_node_found = True
                stack.append(i)
                break
        if not new_node_found:
            stack.pop()
    print(total_visited, total_nodes)
    return total_visited == total_nodes


def check_strongly_connected(edges: [list[list]], total_nodes: int) -> bool:
    if edges is None or len(edges) == 0 or total_nodes <= 0:
        return False
    for i in range(total_nodes):
        all_visit_possible = dfs_from_node(edges, i, total_nodes)
        if not all_visit_possible:
            return False
    return True


def main():
    adj_list = [
        [1, 2],
        [0, 3],
        [0, 4],
        [1, 5],
        [2, 5],
        [3, 4],
        [4],
    ]
    print(check_strongly_connected(adj_list, 7))


if __name__ == '__main__':
    main()
