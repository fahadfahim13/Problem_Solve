def detect_cycle_in_graph_dfs(graph: dict[str, list[str]], node: int) -> bool:
    if graph is None or node <= 0:
        return False
    color = {}
    parent = {}
    for i in graph.keys():
        color[i] = "W"
        parent[i] = None
        
    def dfs(n, col, par):
        col[n] = 'G'
        for vertex in graph[n]:
            if col[vertex] == 'W':
                par[vertex] = n
                dfs(vertex, col, par)
            elif col[vertex] == 'G' and par[n] != vertex:
                print("Cycle found: ", vertex, n)
                return True
        col[n] = 'B'

    for u in graph.keys():
        if color[u] == 'W':
            dfs(u, color, parent)

    return False


def main():
    adj_list = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": ["A", "E"],
        "E": []
    }
    print(detect_cycle_in_graph_dfs(adj_list, 5))


if __name__ == '__main__':
    main()
