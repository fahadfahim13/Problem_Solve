def is_safe(row, col, matrix):
    for i in range(len(matrix)):
        if matrix[row][i]:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if matrix[i][j]:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i < len(matrix) and j >= 0:
        if matrix[i][j]:
            return False
        i += 1
        j -= 1
    return True


def find_queen_position(column: int, mat: list[list[int]]) -> int:
    if column >= len(mat):
        return True
    for i in range(len(mat)):
        if is_safe(i, column, mat):
            mat[i][column] = 1
            if find_queen_position(column + 1, mat):
                return True
        mat[i][column] = 0
    return False


def n_queen_problem(n: int):
    if n is None or n <= 1:
        return None
    matrix = [[0 for i in range(n)] for j in range(n)]
    if not find_queen_position(0, matrix):
        return False
    return matrix


def main():
    n = 3
    ans = n_queen_problem(n)
    if ans:
        for i in ans:
            print(i)
    else:
        print(ans)


if __name__ == '__main__':
    main()
