def mean_array(arr: list[int]) -> float:
    sum = 0
    arr = sorted(arr)
    n = len(arr)
    m = int(round(n * 0.05))
    for i in range(m, n - m):
        sum += arr[i]
    return sum / (n - 2 * m)


def main():
    arr = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10,
           8, 2, 3, 4]
    print(mean_array(arr))


if __name__ == '__main__':
    main()
