def dfs(adj_list: list[list[int]], visited: list, start: int, ans_stack: list) -> (list, list) or None:
    stack = [start]
    while stack:
        temp = stack[-1]
        visited[temp] = True
        new_node = False
        for j in adj_list[temp]:
            if not visited[j]:
                visited[j] = True
                new_node = True
                stack.append(j)
                break
        if not new_node:
            ans_stack.append(stack[-1])
            stack.pop()
    return ans_stack, visited


def topological_sort(adj_list: list[list], total_nodes: int) -> list or None:
    if not adj_list or total_nodes <= 0:
        return None
    visited = [False for i in range(total_nodes)]
    ans_stack = []
    for i in range(total_nodes):
        if not visited[i]:
            ans_stack, visited = dfs(adj_list, visited, i, ans_stack)
    ans_stack.reverse()
    return ans_stack


def main():
    adj_list = [
        [1, 2],
        [3, 4],
        [4],
        [5],
        [5],
        []
    ]
    # adj_list = [
    #     [2, 3],
    #     [],
    #     [],
    #     [1],
    #     [2, 1],
    #     [0, 2]
    # ]
    print(topological_sort(adj_list, len(adj_list)))


if __name__ == "__main__":
    main()

