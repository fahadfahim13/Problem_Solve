def detectCycleInGraph(edges: list[list[int]], node: int) -> bool:
    if edges is None or node == 0:
        return False
    stack = []
    visited = [0 for i in range(0, node)]
    graph = [[] for i in range(0, node)]
    for edge in edges:
        _from = edge[0]
        _to = edge[1]
        graph[_from].append(_to)

    current_node = 0
    visited[current_node] = 1
    stack.append(current_node)
    while len(stack) > 0:
        current_node = stack[-1]
        node_found = False
        for j in graph[current_node]:
            if j in stack:
                print("Cycle found: ", current_node, j)
                return True
            if visited[j] == 0:
                node_found = True
                visited[j] = 1
                stack.append(j)
                break
        if not node_found:
            stack.pop()
    return False


def main():
    arr = [[0, 1], [0, 2], [1, 3], [3, 0], [3, 4]]
    # arr = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(detectCycleInGraph(arr, 5))


if __name__ == '__main__':
    main()
