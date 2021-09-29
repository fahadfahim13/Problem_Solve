import math


def first_occurence_adjacent_differ_1(arr, num):
    if arr is None or num is None:
        return None
    start = 0
    while start < len(arr):
        diff = int(math.fabs(arr[start] - num))
        if diff == 0:
            return start
        start = start + diff

    return -1


if __name__ == "__main__":
    arr = [7, 6, 7, 6, 5, 4, 5, 4, 3, 4, 3, 2]
    print(first_occurence_adjacent_differ_1(arr, 2))
