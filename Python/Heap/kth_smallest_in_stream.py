import heapq as hp


def kth_smallest_in_stream(numbers: list[int], k: int) -> int:
    if numbers is None or k > len(numbers):
        return -1
    arr = []
    hp.heapify(arr)
    for i in range(k):
        hp.heappush(arr, -numbers[i])
    largest = -hp.heappop(arr)
    hp.heappush(arr, -largest)
    for i in range(k, len(numbers)):
        if numbers[i] < largest:
            hp.heappop(arr)
            hp.heappush(arr, -numbers[i])
            largest = -hp.heappop(arr)
            hp.heappush(arr, -largest)
    # largest = -hp.heappop(arr)
    return largest


def main():
    arr = [10, 7, 11, 5, 27, 3, 2, 1]
    k = 6
    print(kth_smallest_in_stream(arr, k))


if __name__ == '__main__':
    main()
