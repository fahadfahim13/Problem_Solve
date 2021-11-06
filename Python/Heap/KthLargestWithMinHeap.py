import heapq


def kth_largest(arr: list[int], k: int) -> int:
    heapq.heapify(arr)
    print(arr)
    for i in range(len(arr) - k + 1):
        maxi = heapq.heappop(arr)
    return maxi


def main():
    arr = [10, 7, 11, 5, 27, 8, 20, 45]
    k = 4
    print(kth_largest(arr, k))


if __name__ == '__main__':
    main()
