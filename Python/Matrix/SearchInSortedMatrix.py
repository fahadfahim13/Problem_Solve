def search_in_sorted_matrix(matrix: list[list[int]], key: int) -> tuple[int, int] or None:
    if matrix is None or len(matrix) <= 0:
        return None
    col = len(matrix) - 1
    row = 0
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == key:
            return row, col
        elif matrix[row][col] > key:
            col -= 1
        else:
            row += 1
    return None


def main():
    matrix = [
        [2, 7, 15],
        [4, 9, 19],
        [6, 10, 24]
    ]
    k = 60
    print(search_in_sorted_matrix(matrix, k))


if __name__ == '__main__':
    main()
