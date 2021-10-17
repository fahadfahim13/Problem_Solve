import heapq as hq


def prims_algorithm(edges: list[list], adj_list: list[list], source: int, total_nodes: int) -> list or None:
    if not adj_list or not edges or total_nodes <= 0:
        return None
    visited = []
    q = [source]
    hq.heapify(q)


def get_adjacency_list(edges: list[list], total_nodes: int) -> list[list[tuple[int, int]]] or None:
    if not edges or total_nodes <= 0:
        return None
    adj_list: list[list[tuple[int, int]]] = [[] for i in range(total_nodes)]
    for i in edges:
        adj_list[i[0]].append((i[1], i[2]))
        adj_list[i[1]].append((i[0], i[2]))
    for i in adj_list:
        i.sort(key=lambda x: x[1])
    for i in adj_list:
        print(i)
    return adj_list


def main():
    edges = [
        [0, 1, 2],
        [0, 2, 4],
        [1, 2, 1],
        [1, 3, 7],
        [2, 4, 3],
        [4, 3, 2],
        [3, 5, 1],
        [4, 5, 5]
    ]
    print(prims_algorithm(edges, get_adjacency_list(edges, 6), 6, 0))


if __name__ == '__main__':
    main()

