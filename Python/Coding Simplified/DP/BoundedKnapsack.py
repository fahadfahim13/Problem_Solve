def bounded_knapsack(weight: list[int], profit: list[int], capacity: int) -> int:
    if weight is None or profit is None:
        return 0
    profit_weight = [[0 for i in range(capacity + 1)] for j in range(len(weight))]
    for i in range(len(weight)):
        for j in range(capacity + 1):
            if weight[i] <= j:
                included_weight = profit[i] + profit_weight[i - 1][j - weight[i]]
                excluded_weight = profit_weight[i - 1][j]
                profit_weight[i][j] = max(included_weight, excluded_weight)
            else:
                profit_weight[i][j] = max(profit_weight[i - 1][j], profit_weight[i][j - 1])
    return profit_weight[-1][-1]


def main():
    weight = [1, 2, 3, 5]
    profit = [3, 5, 7, 10]
    capacity = 8
    print(bounded_knapsack(weight, profit, capacity))


if __name__ == '__main__':
    main()
