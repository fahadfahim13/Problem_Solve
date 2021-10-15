def dfs(adj_list: list[list[int]], nodes: int) -> bool or None:
    if adj_list is None or len(adj_list) == 0 or nodes <= 0:
        return False
    visited = [False for i in range(nodes)]
    stack = [0]
    while len(stack) > 0:
        temp = stack[-1]
        print(stack)
        if not visited[temp]:
            visited[temp] = True
        adjacent_node_found = False
        for i in adj_list[temp]:
            if not visited[i]:
                adjacent_node_found = True
                stack.append(i)
                break
        if not adjacent_node_found:
            stack.pop()
    for i in visited:
        if not i:
            return False
    return True


def main():
    edges = [
        [1, 2],
        [0, 3],
        [0, 4],
        [1, 5],
        [2, 5],
        [3, 4],
        [7],
        []
    ]
    print(dfs(edges, 8))


if __name__ == '__main__':
    main()
