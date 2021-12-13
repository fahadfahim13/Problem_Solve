def rotate(matrix: list[list[int]]) -> None:
    _l, _r = 0, len(matrix) - 1
    while _l < _r:
        for c in range(_r - 1):
            _t, _b = _l, _r - 1
            temp = matrix[_t][_l + c]
            matrix[_t][_l + c] = matrix[_b - c][_l]
            matrix[_b - c][_l] = matrix[_b][_r - c]
            matrix[_b][_r - c] = matrix[_t + c][_r]
            matrix[_t + c][_r] = temp
        _r -= 1
        _l += 1


def main():
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix)
    print(matrix)


if __name__ == '__main__':
    main()
