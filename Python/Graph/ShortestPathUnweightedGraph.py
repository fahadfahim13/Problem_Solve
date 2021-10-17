import math


def shortest_path_bfs(adj_list: list[list], total_nodes: int, start: int) -> list or None:
    if not adj_list or total_nodes <= 0:
        return None
    distance: list = [math.inf for i in range(total_nodes)]
    distance[start] = 0
    q = [start]
    previous = [i for i in range(total_nodes)]
    while q:
        temp = q[0]
        for i in adj_list[temp]:
            if distance[i] > distance[temp] + 1:
                distance[i] = distance[temp] + 1
                previous[i] = temp
                q.append(i)
    return distance


def main():
    adj_list = [
        [1, 3],
        [3, 4],
        [0, 5],
        [5, 6],
        [6],
        [],
        [5]
    ]
    print(shortest_path_bfs(adj_list, len(adj_list), 2))


if __name__ == '__main__':
    main()
