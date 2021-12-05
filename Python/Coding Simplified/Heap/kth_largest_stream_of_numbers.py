import heapq


def kth_largest_stream_of_numbers(arr: list[int], k: int) -> int:
    heap_arr = []
    heapq.heapify(heap_arr)
    kth_largest = 0
    for i in range(k):
        heapq.heappush(heap_arr, arr[i])
    kth_largest = heap_arr[0]
    for i in range(k, len(arr)):
        if arr[i] > kth_largest:
            heapq.heappop(heap_arr)
            heapq.heappush(heap_arr, arr[i])
            kth_largest = heap_arr[0]

    return kth_largest


def main():
    arr = [10, 7, 11, 5, 27, 8, 9, 45]
    k = 5
    print(kth_largest_stream_of_numbers(arr, k))


if __name__ == '__main__':
    main()
