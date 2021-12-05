import heapq as hp


def top_k_largest_values_in_array(numbers: list[int], k: int) -> list[int] or None:
    if numbers is None or k > len(numbers):
        return None
    arr = []
    hp.heapify(arr)
    for i in range(k):
        hp.heappush(arr, numbers[i])
    largest = hp.heappop(arr)
    hp.heappush(arr, largest)
    for i in range(k, len(numbers)):
        if numbers[i] > largest:
            hp.heappop(arr)
            hp.heappush(arr, numbers[i])
            largest = hp.heappop(arr)
            hp.heappush(arr, largest)
    return sorted(arr, reverse=True)


def main():
    arr = [10, 7, 11, 30, 8, 38, 2, 45]
    k = 3
    print(top_k_largest_values_in_array(arr, k))


if __name__ == '__main__':
    main()
