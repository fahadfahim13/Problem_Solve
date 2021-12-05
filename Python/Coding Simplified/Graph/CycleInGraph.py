def dfs(adj_list: list[list[int]], total_nodes: int, start: int, parent: int, visited: list) -> list[bool] or bool:
    if adj_list is None or total_nodes <= 0 or visited is None or len(adj_list) == 0 or len(visited) == 0:
        return False
    stack = [start]
    visited[start] = True
    for i in adj_list[start]:
        if not visited[i]:
            visited, cycle_preset = dfs(adj_list, total_nodes, i, start, visited)
        elif i != parent:
            return visited, True
    return visited, False


def is_cycle_present(adj_list: list[list[int]], total_nodes: int) -> bool:
    if adj_list is None or total_nodes <= 0 or len(adj_list) == 0:
        return False
    visited = [False for i in range(total_nodes)]
    for i in range(total_nodes):
        if not visited[i]:
            visited, cycle_present = dfs(adj_list, total_nodes, i, -1, visited)
            if cycle_present:
                print(i)
                return cycle_present
    return False


def main():
    adj_list = [
        [1],
        [2, 3, 0],
        [1, 3],
        [2, 1]
    ]
    print(is_cycle_present(adj_list, len(adj_list)))


if __name__ == '__main__':
    main()
