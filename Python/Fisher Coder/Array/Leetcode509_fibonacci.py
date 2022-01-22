def fibonacci(n: int) -> int:
    arr = [0, 1]
    if n >= len(arr):
        for i in range(2, n + 1):
            arr.append(arr[i - 1] + arr[i - 2])
    return arr[n]


def main():
    n = 40
    print(fibonacci(n))


if __name__ == '__main__':
    main()
