def diagonal_sum(arr: list) -> int or None:
    if arr is None:
        return None
    sum_nums = 0
    # for i in range(0, len(arr)):
    #     for j in range(0, len(arr)):
    #         if i == j:
    #             sum_nums += arr[i][j]

    for i in range(0, len(arr)):
        sum_nums += arr[i][i]
    return sum_nums


def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(diagonal_sum(arr))


if __name__ == '__main__':
    main()
