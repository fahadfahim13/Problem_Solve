def detect_cycle_directed_graph(graph: list[list[int]], num_of_nodes: int) -> bool:
    if graph is None or num_of_nodes <= 0:
        return False
    stack = []
    visited = [0 for i in range(num_of_nodes)]
    stack.append(0)
    while len(stack) > 0:
        i = stack[-1]
        if visited[i] == 0:
            visited[i] = 1
            new_node_found = False
            for j in graph[i]:
                if visited[j] and j in stack:
                    return True
                elif visited[j] == 0:
                    new_node_found = True
                    stack.append(j)
                    break
            if not new_node_found:
                stack.pop()
