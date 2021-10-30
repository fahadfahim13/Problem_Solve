import math


def min_diff_partition(arr: list[int]) -> int:
    if arr is None:
        return 0
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[1] - arr[2]
    mid = sum(arr) // 2
    bool_arr = [[False for i in range(mid + 1)] for j in range(len(arr))]
    for i in range(len(arr)):
        bool_arr[i][0] = True
    for j in range(mid + 1):
        if j == arr[0]:
            bool_arr[0][j] = True
    for i in range(1, len(arr)):
        for j in range(1, mid + 1):
            if bool_arr[i - 1][j]:
                bool_arr[i][j] = True
            elif j >= arr[i]:
                bool_arr[i][j] = bool_arr[i - 1][j - arr[i]]
    first_part = - math.inf
    for i in range(mid, -1, -1):
        if bool_arr[len(arr)-1][i]:
            first_part = i
            break
    second_part = sum(arr) - first_part
    return second_part - first_part


def main():
    arr = [1, 2, 3, 5, 13]
    print(min_diff_partition(arr))


if __name__ == '__main__':
    main()
