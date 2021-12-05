def kahn_algorithm_topological_sort(adj_list: list[list], total_nodes: int) -> list or None:
    if not adj_list or total_nodes <= 0:
        return None
    in_degree = {i: 0 for i in range(total_nodes)}
    for i in adj_list:
        for j in i:
            in_degree[j] += 1
    visited = [False for i in range(total_nodes)]
    q = []
    count = 0
    ans_list = []
    for i in in_degree:
        if in_degree[i] == 0:
            q.append(i)
    while q:
        temp = q[0]
        ans_list.append(q.pop(0))
        visited[temp] = True
        count += 1
        for i in adj_list[temp]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    if count != total_nodes:
        return None
    return ans_list


def main():
    adj_list = [
        [],
        [],
        [1],
        [0, 2],
        [0, 1],
        [0, 3]
    ]
    print(kahn_algorithm_topological_sort(adj_list, len(adj_list)))


if __name__ == "__main__":
    main()
