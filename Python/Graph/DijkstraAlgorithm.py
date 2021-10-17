import math
import heapq


def dijkstra_algorithm(edges: list[list], total_nodes: int, source: int) -> list or None:
    if not edges or total_nodes <= 0:
        return None
    distance = [math.inf for i in range(total_nodes)]
    distance[source] = 0
    pq = [source]
    heapq.heapify(pq)

    while pq:
        temp = heapq.heappop(pq)
        for j in edges:
            if j[0] == temp:
                if distance[j[1]] > distance[temp] + j[2]:
                    distance[j[1]] = distance[temp] + j[2]
                    heapq.heappush(pq, j[1])
    print(distance)


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
    print(dijkstra_algorithm(edges, 6, 0))


if __name__ == '__main__':
    main()
