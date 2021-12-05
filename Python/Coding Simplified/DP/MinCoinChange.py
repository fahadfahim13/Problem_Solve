def min_coin_change(coins: list[int], _sum: int) -> int:
    if coins is None or _sum is None:
        return 0
    total_arr = [[0 for i in range(_sum + 1)] for j in range(len(coins))]
    for i in range(len(coins)):
        for j in range(_sum + 1):
            if coins[i] <= j:
                if i > 0:
                    total_arr[i][j] = min(total_arr[i - 1][j], 1 + total_arr[i][j - coins[i]])
                else:
                    total_arr[i][j] = 1 + total_arr[i][j - coins[i]]
            else:
                total_arr[i][j] = total_arr[i - 1][j]
        print(total_arr[i])
    return total_arr[-1][-1]


def main():
    coins = [1, 2, 3]
    _sum = 5
    print(min_coin_change(coins, _sum))


if __name__ == '__main__':
    main()
