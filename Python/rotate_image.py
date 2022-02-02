import numpy as np


def rotate_image(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(0, n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(0, n):
        l = 0
        r = n - 1
        while l < r:
            matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_image(matrix)
    print(np.matrix(matrix))


if __name__ == '__main__':
    main()
