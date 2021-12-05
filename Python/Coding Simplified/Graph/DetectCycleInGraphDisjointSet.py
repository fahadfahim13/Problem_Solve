def find_parent(node: int, parent: list[int]) -> int or None:
    if node is None or parent is None:
        return None
    if parent[node] == node:
        return node
    return find_parent(parent[node], parent)


def detect_cycle_disjoint_set(edges: list[list[int]], node: int) -> bool:
    if edges is None or node <= 0:
        return False
    parent = [i for i in range(node)]
    for edge in edges:
        _from = edge[0]
        _to = edge[1]
        _parent_from = find_parent(_from, parent)
        _parent_to = find_parent(_to, parent)
        if _parent_from != _parent_to:
            parent[_to] = _parent_from
        else:
            print("Cycle Found: ", _from, _to)
            return True
    return False


def main():
    edges = [[0, 1], [0, 2], [1, 3], [3, 0], [3, 4]]
    print(detect_cycle_disjoint_set(edges, 5))


if __name__ == '__main__':
    main()
