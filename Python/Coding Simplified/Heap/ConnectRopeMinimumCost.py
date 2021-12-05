import heapq as hp


def connect_ropes_minimum_cost(ropes: list[int]) -> int:
    if ropes is None:
        return 0
    arr = []
    hp.heapify(arr)
    for rope in ropes:
        hp.heappush(arr, rope)
    count = 0
    while len(arr):
        el1 = hp.heappop(arr)
        el2 = hp.heappop(arr)
        count += (el1 + el2)
        if len(arr):
            hp.heappush(arr, (el1 + el2))
    return count


def main():
    ropes = [3, 4, 7, 2]
    print(connect_ropes_minimum_cost(ropes))


if __name__ == '__main__':
    main()
