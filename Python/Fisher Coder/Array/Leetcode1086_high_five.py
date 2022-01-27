import heapq as hp


def high_five(numbers: list[list[int]]) -> list[list[int, float]] or None:
    if len(numbers) == 0:
        return None
    calc = {}
    res = []
    for num in numbers:
        if num[0] in calc:
            hp.heappush(calc[num[0]], -num[1])
        else:
            calc[num[0]] = [-num[1]]
            hp.heapify(calc[num[0]])

    keys = sorted(calc.keys())
    for i in keys:
        n = 0
        total = 0
        while n < 5:
            numb = hp.heappop(calc[i])
            total += -numb
            n += 1
        res.append([i, total // 5])

    return res


def main():
    numbers = [[2, 95], [1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100],
           [2, 76]]
    print(high_five(numbers))


if __name__ == '__main__':
    main()
