def fibonacci(n: int) -> int:
    if n < 2:
        return n
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])
    print(arr)
    return arr[-1]


def main():
    n = int(input())
    print(fibonacci(n))


if __name__ == '__main__':
    main()
