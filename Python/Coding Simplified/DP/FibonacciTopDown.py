def fibonacci(arr: list, n: int) -> int or None:
    if n < 2:
        return n
    if arr[n] == 0:
        arr[n] = fibonacci(arr, n - 1) + fibonacci(arr, n - 2)
    return arr[n]


def main():
    n = int(input())
    arr = [0 for i in range(n + 1)]
    print(fibonacci(arr, n))


if __name__ == '__main__':
    main()
