import numpy


def is_fresh(matrix: list[list[int]], row: int, col: int, visited: list[list[bool]]):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[row]) and matrix[row][col] == 1 and \
           not visited[row][col]


def bfs(oranges, row, col, visited, rotten_queue):
    visited[row][col] = True
    if is_fresh(oranges, row - 1, col, visited):
        oranges[row - 1][col] = 2
        rotten_queue.append((row-1, col))
    if is_fresh(oranges, row, col - 1, visited):
        oranges[row][col - 1] = 2
        rotten_queue.append((row, col - 1))
    if is_fresh(oranges, row, col + 1, visited):
        oranges[row][col + 1] = 2
        rotten_queue.append((row, col + 1))
    if is_fresh(oranges, row + 1, col, visited):
        oranges[row + 1][col] = 2
        rotten_queue.append((row + 1, col))


def min_time_to_rot_oranges(oranges: list[list[int]], row: int, col: int) -> int or None:
    if oranges is None or len(oranges) <= 0:
        return None
    visited = [[False for j in range(col)] for i in range(row)]
    count = 0
    rotten_queue = []
    for i in range(row):
        for j in range(col):
            if oranges[i][j] == 2 and not visited[i][j]:
                rotten_queue.append((i, j))
    rotten_queue.append((-1, -1))
    is_found = False
    while len(rotten_queue):
        el = rotten_queue.pop(0)
        if el != (-1, -1):
            bfs(oranges, el[0], el[1], visited, rotten_queue)
        else:
            if len(rotten_queue):
                count += 1
                rotten_queue.append((-1, -1))
    return count


def main():
    oranges = [
        [0, 2, 0, 0, 2],
        [0, 1, 0, 1, 1],
        [0, 1, 0, 1, 2],
        [2, 1, 0, 2, 0]
    ]
    # print(numpy.matrix(oranges))
    print(min_time_to_rot_oranges(oranges, len(oranges), len(oranges[0])))


if __name__ == '__main__':
    main()
