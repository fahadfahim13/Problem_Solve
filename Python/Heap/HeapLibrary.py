import heapq


def HeapLibrary(li: list[int]):
    heapq.heapify(li)
    print(li)
    heapq.heappush(li, 4)
    print(li)
    heapq.heappush(li, 2)
    print(li)
    heapq.heappush(li, 6)
    print(li)
    heapq.heappush(li, 0)
    print(li)
    print(heapq.heappop(li))
    print(li)
    heapq.heappushpop(li, 0)
    print(li)


def main():
    arr = [5, 7, 9, 1, 3]
    HeapLibrary(arr)


if __name__ == '__main__':
    main()
