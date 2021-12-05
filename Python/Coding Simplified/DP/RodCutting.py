def rod_cutting(length: list[int], price: list[int], l: int) -> int:
    if length is None or price is None:
        return 0
    profit_arr = [[0 for i in range(l + 1)] for j in range(len(length))]
    for i in range(l + 1):
        profit_arr[0][i] = (i // length[0]) * price[0]
    for i in range(len(length)):
        profit_arr[i][0] = 0
    for i in range(1, len(length)):
        for j in range(l + 1):
            if j < length[i]:
                profit_arr[i][j] = profit_arr[i - 1][j]
            else:
                profit_arr[i][j] = max(profit_arr[i - 1][j], price[i] + profit_arr[i][j - length[i]])
        print(profit_arr[i])
    return profit_arr[-1][-1]


def main():
    length = [1, 2, 3, 4, 5]
    price = [3, 5, 10, 11, 15]
    l = 5
    print(rod_cutting(length, price, l))


if __name__ == '__main__':
    main()
