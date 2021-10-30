def print_arr(arr: list[list]) -> None:
    for i in range(len(arr)):
        print(arr[i])


def equal_sum_partition(arr: list[int]) -> False:
    if arr is None or sum(arr) % 2 == 1:
        return False
    sub_sum = sum(arr) // 2
    bool_arr = [[False for i in range(sub_sum + 1)] for j in range(len(arr))]
    for i in range(len(arr)):
        bool_arr[i][0] = True
    for j in range(sub_sum + 1):
        if j == arr[0]:
            bool_arr[0][j] = True
    for i in range(1, len(arr)):
        for j in range(1, sub_sum + 1):
            if bool_arr[i - 1][j]:
                bool_arr[i][j] = True
            elif j >= arr[i]:
                bool_arr[i][j] = bool_arr[i - 1][j - arr[i]]

    return bool_arr[-1][-1]


def main():
    arr = [1, 2, 3, 5, 9]
    print(equal_sum_partition(arr))


if __name__ == '__main__':
    main()
