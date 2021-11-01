def max_sum_consecutive_not_allowed(arr: list[int]) -> int:
    if arr is None or len(arr) == 0:
        return 0
    sum_arr = [0 for i in range(len(arr))]
    sum_arr[0] = arr[0]
    sum_arr[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        sum_arr[i] = max(sum_arr[i-1], arr[i] + sum_arr[i-2])
    print(sum_arr)
    return sum_arr[-1]


def main():
    arr = [4, 2, 3, 5, 1, 6, 7]
    print(max_sum_consecutive_not_allowed(arr))


if __name__ == '__main__':
    main()
