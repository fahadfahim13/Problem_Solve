def find_less_or_equal_sorted_matrix(matrix: list[list[int]], key: int) -> int or None:
    if matrix is None or len(matrix) <= 0:
        return None
    row = 0
    col = len(matrix) - 1
    count = 0
    while row < len(matrix) and col >= 0:
        if matrix[row][col] <= key:
            count += col + 1
            row += 1
        else:
            col -= 1
    return count


def main():
    matrix = [
        [2, 7, 15],
        [4, 9, 19],
        [6, 10, 24]
    ]
    k = 4
    print(find_less_or_equal_sorted_matrix(matrix, k))


if __name__ == '__main__':
    main()
