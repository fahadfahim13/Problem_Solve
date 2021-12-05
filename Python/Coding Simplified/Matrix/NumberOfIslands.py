import numpy as np


def is_safe(matrix, row, col, visited):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[row]) and matrix[row][col] == 1 and not visited[row][col]


def dfs(matrix: list[list[int]], row: int, col: int, visited: list[list[bool]]):
    visited[row][col] = True
    if is_safe(matrix, row - 1, col - 1, visited):
        dfs(matrix, row - 1, col - 1, visited)
    if is_safe(matrix, row - 1, col, visited):
        dfs(matrix, row - 1, col, visited)
    if is_safe(matrix, row - 1, col + 1, visited):
        dfs(matrix, row - 1, col + 1, visited)
    if is_safe(matrix, row, col - 1, visited):
        dfs(matrix, row, col - 1, visited)
    if is_safe(matrix, row, col + 1, visited):
        dfs(matrix, row, col + 1, visited)
    if is_safe(matrix, row + 1, col - 1, visited):
        dfs(matrix, row + 1, col - 1, visited)
    if is_safe(matrix, row + 1, col, visited):
        dfs(matrix, row + 1, col, visited)
    if is_safe(matrix, row + 1, col + 1, visited):
        dfs(matrix, row + 1, col + 1, visited)


def number_of_islands(matrix: list[list[int]], row: int, col: int) -> int or None:
    if matrix is None or len(matrix) <= 0:
        return None
    visited = [[False for i in range(col)] for j in range(row)]
    count = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(matrix, i, j, visited)
                count += 1
    return count


def main():
    islands = [
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1]
    ]
    print(np.matrix(islands))
    print(number_of_islands(islands, 5, 5))


if __name__ == '__main__':
    main()
