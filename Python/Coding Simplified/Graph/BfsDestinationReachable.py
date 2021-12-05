from queue import Queue


def bfs(adj_list: list[list[int]], start_node: int, total_node: int, visited: list[bool]) -> list[bool] or None:
    if adj_list is None or len(adj_list) == 0 or total_node <= 0:
        return None
    q = Queue()
    q.put(start_node)
    while not q.empty():
        temp = q.get()
        if not visited[temp]:
            visited[temp] = True
        for i in adj_list[temp]:
            if not visited[i]:
                q.put(i)
    return visited


def check_source_to_destination(adj_list: list[list[int]], source: int, dest: int, total_nodes: int) -> bool:
    if adj_list is None or len(adj_list) == 0 or total_nodes <= 0:
        return False
    visited = [False for i in range(total_nodes)]
    new_visited = bfs(adj_list, source, total_nodes, visited)
    return new_visited[dest]


def main():
    adj_list = [
        [1],
        [2],
        [0],
        [2]
        ##########
        # [1, 2],
        # [0, 3],
        # [0],
        # [1],
        # [5],
        # [4, 6],
        # [5]
    ]
    source = 0
    dest = len(adj_list) - 1
    print(check_source_to_destination(adj_list, source, dest, len(adj_list)))


if __name__ == '__main__':
    main()
