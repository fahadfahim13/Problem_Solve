import math


def first_occurance_with_adjacent_k(arr, num, k):
    if arr is None or num is None:
        return None
    start = 0

    while start < len(arr):
        if arr[start] == num:
            return start
        diff = int(math.fabs(arr[start] - num) / k)
        start = start + max(1, diff)

    return -1


if __name__ == "__main__":
    arr = [70, 83, 90, 100, 110, 120, 130, 113, 119, 134]
    print(first_occurance_with_adjacent_k(arr, 83, 20))
