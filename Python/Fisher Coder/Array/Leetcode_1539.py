def kth_missing(arr: list[int], k: int) -> int:
    missing_count = arr[-1] - len(arr)
    if k < arr[0]:
        return k
    if k > missing_count:
        return arr[-1] + (k - missing_count)
    missed = arr[0] - 1
    for i in range(1, len(arr)):
        missed += arr[i] - arr[i - 1] - 1
        if missed >= k:
            return arr[i] - (missed - k) - 1


def main():
    arr = [2, 3, 4, 7, 11]
    # arr = [1, 10, 21, 22, 25]
    k = 5
    print(kth_missing(arr, k))


if __name__ == '__main__':
    main()
