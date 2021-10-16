def bfs(adj_list: list[list], total_nodes: int) -> bool or None:
    in_degree = {i: 0 for i in range(total_nodes)}
    for i in adj_list:
        for j in i:
            if j in in_degree:
                in_degree[j] += 1
    q = []
    # print(in_degree)
    visited = [False for i in range(total_nodes)]
    total_visited = 0
    for i in in_degree:
        if in_degree[i] == 0:
            q.append(i)
    while q:
        total_visited += 1
        temp = q[0]
        q.remove(q[0])
        for i in adj_list[temp]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    return total_nodes != total_visited


def main():
    adj_list = [
        [1, 3],
        [2],
        [3],
        []
    ]
    print(bfs(adj_list, len(adj_list)))


if __name__ == '__main__':
    main()
