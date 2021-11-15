import math


def print_sudoku(sudoku: list[list[int]]) -> None:
    for i in sudoku:
        print(i)


def is_safe(row, col, value, sudoku) -> bool:
    for i in range(len(sudoku)):
        if sudoku[row][i] == value:
            # print(f"Found match in row -> Row: {row}, Col: {i}, Value {value}")
            return False
    for j in range(len(sudoku)):
        if sudoku[j][col] == value:
            # print(f"Found match in column -> Row: {j}, Col: {col}, Value {value}")
            return False
    sqrt = int(math.sqrt(len(sudoku)))
    row_start = row - row % sqrt
    col_start = col - col % sqrt
    for i in range(row_start, row_start + sqrt):
        for j in range(col_start, col_start + sqrt):
            if sudoku[i][j] == value:
                # print(f"Found match in box -> Row: {i}, Col: {j}, Value {value}")
                return False
    return True


def sudoku_solve(sudoku: list[list[int]]) -> bool or None:
    if sudoku is None or len(sudoku) <= 0:
        return False
    is_empty = True
    row = -1
    col = -1
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                is_empty = False
                row = i
                col = j
                break
        if not is_empty:
            break
    if is_empty:
        return True
    for num in range(1, len(sudoku) + 1):
        if is_safe(row, col, num, sudoku):
            sudoku[row][col] = num
            if sudoku_solve(sudoku):
                return True
            else:
                sudoku[row][col] = 0

    return False


def main():
    sudoku = [
        [0, 2, 3, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [2, 4, 1, 0]
    ]
    ans = sudoku_solve(sudoku)
    if ans:
        print_sudoku(sudoku)
    else:
        print(False)


if __name__ == '__main__':
    main()
