import heapq as hp


def heap_sort(numbers: list[int]) -> list[int] or None:
    if numbers is None or len(numbers) <= 0:
        return None
    hp.heapify(numbers)
    arr = []
    while numbers:
        arr.append(hp.heappop(numbers))
    return arr


def main():
    arr = [10, 7, 11, 30, 8, 38, 2, 45]
    print(heap_sort(arr))


if __name__ == '__main__':
    main()
