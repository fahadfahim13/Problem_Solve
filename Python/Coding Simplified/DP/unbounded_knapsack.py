def unbounded_knapsack(weight: list[int], profit: list[int], capacity: int) -> int:
    if weight is None or profit is None:
        return 0
    bool_arr = [[0 for i in range(capacity + 1)] for j in range(len(weight))]
    for i in range(len(weight)):
        bool_arr[i][0] = 0
    for i in range(capacity + 1):
        bool_arr[0][i] = (i // weight[0]) * profit[0]
    # print(bool_arr[0])
    for i in range(1, len(weight)):
        for j in range(1, capacity + 1):
            if j < weight[i]:
                bool_arr[i][j] = bool_arr[i - 1][j]
            else:
                bool_arr[i][j] = max(bool_arr[i-1][j], profit[i] + bool_arr[i][j - weight[i]])
        # print(bool_arr[i])
    return bool_arr[-1][-1]


def main():
    weight = [1, 2, 3, 5]
    profit = [1, 4, 7, 10]
    capacity = 8
    print(unbounded_knapsack(weight, profit, capacity))


if __name__ == '__main__':
    main()
