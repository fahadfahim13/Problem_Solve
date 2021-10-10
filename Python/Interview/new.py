def getNthFibonacci(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo[-1]


def main():
    n = 8
    print(getNthFibonacci(n))


if __name__ == '__main__':
    main()
