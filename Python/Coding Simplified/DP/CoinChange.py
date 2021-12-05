def coin_change(coins: list[int], _sum: int) -> int:
    if coins is None:
        return 0
    total_arr = [[0 for i in range(_sum + 1)] for j in range(len(coins))]
    for j in range(len(coins)):
        total_arr[j][0] = 1

    for i in range(len(coins)):
        for j in range(_sum + 1):
            if coins[i] > j:
                total_arr[i][j] = total_arr[i-1][j]
            else:
                if i > 0:
                    total_arr[i][j] = total_arr[i - 1][j] + total_arr[i][j - coins[i]]
                else:
                    total_arr[i][j] = total_arr[i][j - coins[i]]
        print(total_arr[i])
    return total_arr[-1][-1]


def main():
    coins = [1, 2, 3]
    _sum = 5
    print(coin_change(coins, _sum))


if __name__ == '__main__':
    main()
