def number_of_ways(n: int) -> int:
    if n < 1:
        return n
    ways = [1]
    for i in range(1, n+1):
        _sum = ways[i - 1]
        if i - 2 >= 0:
            _sum += (ways[i - 2])
        if i - 3 >= 0:
            _sum += (ways[i - 3])
        ways.append(_sum)
    print(ways)
    return ways[n]


def main():
    n = int(input())
    print(number_of_ways(n))


if __name__ == '__main__':
    main()
