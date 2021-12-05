import math
import heapq as hp


def closest_point_to_origin_max_heap(points: list[tuple[int, int]], k: int) -> list[tuple[int, int]] or None:
    if points is not None and len(points) > 0 and 0 < k <= len(points):
        distances = {}
        for point in points:
            if point not in distances:
                distances[point] = math.sqrt(point[0]*point[0] + point[1]*point[1])
        # print(distances)
        arr = []
        hp.heapify(arr)
        c = 0
        for dist in distances:
            if c >= k:
                break
            hp.heappush(arr, (-distances[dist], dist))
            c += 1
        largest = hp.heappop(arr)
        hp.heappush(arr, largest)
        c = 0
        for dist in distances:
            if c >= k:
                if distances[dist] < -largest[0]:
                    hp.heappop(arr)
                    hp.heappush(arr, (-distances[dist], dist))
                    largest = hp.heappop(arr)
                    hp.heappush(arr, largest)
            c += 1
        ans = []
        for i in range(k):
            el = hp.heappop(arr)
            ans.append(el[1])
        return ans
    return None


def closest_point_to_origin(points: list[tuple[int, int]], k: int) -> list[tuple[int, int]] or None:
    if points is None or len(points) <= 0 or k <= 0 or k > len(points):
        return None
    distances = {}
    for point in points:
        if point not in distances:
            distances[point] = math.sqrt(point[0]*point[0] + point[1]*point[1])
    # print(distances)
    arr = []
    hp.heapify(arr)
    for dist in distances:
        hp.heappush(arr, (distances[dist], dist))
    ans = []
    # print(arr)
    for i in range(k):
        el = hp.heappop(arr)
        ans.append(el[1])
    return ans


def main():
    points = [(1, 4), (2, 3), (3, 5), (-3, 2), (-3, -4), (-1, -1), (1, -2)]
    k = 4
    print(closest_point_to_origin_max_heap(points, k))
    print(closest_point_to_origin(points, k))


if __name__ == '__main__':
    main()
