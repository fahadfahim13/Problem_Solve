def target_sum(arr: list[int], given_sum: int) -> int:
    if arr is None or given_sum is None or sum(arr) < given_sum or (sum(arr) + given_sum) % 2 != 0:
        return 0
    actual_sum = (sum(arr) + given_sum) // 2
    count_arr = [[0 for j in range(actual_sum + 1)] for i in range(len(arr))]
    for i in range(len(arr)):
        count_arr[i][0] = 1
    for j in range(actual_sum + 1):
        if j == arr[0]:
            count_arr[0][j] = 1
    for i in range(1, len(arr)):
        for j in range(actual_sum + 1):
            if j < arr[i]:
                count_arr[i][j] = count_arr[i - 1][j]
            else:
                count_arr[i][j] = count_arr[i - 1][j - arr[i]] + count_arr[i - 1][j]
        print(count_arr[i])
    return count_arr[-1][-1]


def main():
    arr = [1, 2, 1, 3]
    given_sum = 3
    print(target_sum(arr, given_sum))


if __name__ == '__main__':
    main()
