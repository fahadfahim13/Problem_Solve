def dfs(adj_list: list[list[int]], start_node: int, total_nodes: int, visited: list[bool]) -> list[bool] or None:
    if adj_list is None or len(adj_list) == 0 or total_nodes <= 0 or visited is None:
        return None
    stack = [start_node]
    while len(stack) > 0:
        temp = stack[-1]
        if not visited[temp]:
            visited[temp] = True
        new_node_found = False
        for i in adj_list[temp]:
            if not visited[i]:
                new_node_found = True
                stack.append(i)
                break
        if not new_node_found:
            stack.pop()
    return visited


def total_connected_components(adj_list: list[list[int]], total_nodes: int) -> int or None:
    if adj_list is None or len(adj_list) == 0 or total_nodes <= 0:
        return None
    visited = [False for i in range(total_nodes)]
    count = 0
    for i in range(total_nodes):
        if not visited[i]:
            visited = dfs(adj_list, i, total_nodes, visited)
            count += 1

    return count


def main():
    adj_list = [
        [1, 2],
        [0, 3],
        [0],
        [1],
        [5],
        [4, 6],
        [5]
    ]
    print(total_connected_components(adj_list, len(adj_list)))


if __name__ == '__main__':
    main()
