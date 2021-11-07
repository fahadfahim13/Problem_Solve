import heapq


def kth_largest(arr: list[int], k: int) -> int:
    heapq.heapify(arr)
    print(arr)
    maxi = -1
    for i in range(len(arr) - k + 1):
        maxi = heapq.heappop(arr)
    return maxi


def kth_largest_min_heap(arr: list[int], k: int) -> int:
    k_arr = []
    k_large = 0
    for i in range(0, k):
        k_arr.append(arr[i])
    heapq.heapify(k_arr)
    k_large = k_arr[0]
    for i in range(k, len(arr)):
        if arr[i] > k_large:
            heapq.heappop(k_arr)
            heapq.heappush(k_arr, arr[i])
            k_large = k_arr[0]
    return k_large


def main():
    arr = [10, 7, 11, 5, 27, 8, 20, 45]
    k = 3
    # print(kth_largest(arr, k))
    print(kth_largest_min_heap(arr, k))


if __name__ == '__main__':
    main()
