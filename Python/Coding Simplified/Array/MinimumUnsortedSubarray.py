import math


def minimum_unsorted_subarray(arr: list) -> (int, int):
    start = 0
    end = len(arr) - 1
    while start < end:
        start_next = start + 1
        if arr[start_next] < arr[start]:
            break
        start += 1

    while start < end:
        end_prev = end - 1
        if arr[end_prev] > arr[end]:
            break
        end -= 1
    min_el, max_el = min(arr[i] for i in range(start, end + 1)), max(arr[i] for i in range(start, end + 1))
    for i in range(0, start):
        if arr[i] > min_el:
            start = i
            break
    for i in range(len(arr) - 1, end, -1):
        if arr[i] < max_el:
            end = i
            break
    return start, end


def main():
    arr = [1, 2, 5, 3, 6, 10, 9, 21, 25]
    arr2 = [1, 2, 5, 3, 0, 12, 13, 8, 15, 18]
    arr3 = [1, 2, 5, 3, 6, 12, 19, 8, 15, 18]
    print(minimum_unsorted_subarray(arr))
    print(minimum_unsorted_subarray(arr2))
    print(minimum_unsorted_subarray(arr3))


if __name__ == '__main__':
    main()
