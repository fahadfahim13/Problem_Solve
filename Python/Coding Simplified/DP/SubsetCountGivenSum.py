def subset_count_given_sum(arr: list[int], given_sum: int) -> int:
    if arr is None or given_sum is None:
        return 0
    count_arr = [[0 for i in range(given_sum + 1)] for j in range(len(arr))]
    for i in range(len(arr)):
        count_arr[i][0] = 1
    for i in range(given_sum + 1):
        if i == arr[0]:
            count_arr[0][i] = 1
    print(count_arr[0])
    for i in range(1, len(arr)):
        for j in range(1, given_sum + 1):
            if j < arr[i]:
                count_arr[i][j] = count_arr[i - 1][j]
            else:
                count_arr[i][j] = count_arr[i - 1][j] + count_arr[i - 1][j - arr[i]]
        print(count_arr[i])
    return count_arr[-1][-1]


def main():
    arr = [2, 3, 7, 1, 4, 5]
    given_sum = 7
    print(subset_count_given_sum(arr, given_sum))


if __name__ == '__main__':
    main()
