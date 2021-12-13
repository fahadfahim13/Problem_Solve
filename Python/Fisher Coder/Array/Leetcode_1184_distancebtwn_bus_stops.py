def distanceBetweenBusStops(distance: list[int], start: int, destination: int) -> int:
    total = sum(distance)
    short_dist = 0
    _s = start
    _d = destination
    if start > destination:
        _s = destination
        _d = start
    for i in range(_s, _d):
        short_dist += distance[i]
    if short_dist < (total - short_dist):
        return short_dist
    return total - short_dist


def main():
    # distance = [1, 2, 3, 4]
    distance = [7, 10, 1, 12, 11, 14, 5, 0]
    start = 7
    destination = 2
    print(distanceBetweenBusStops(distance, start, destination))


if __name__ == '__main__':
    main()
